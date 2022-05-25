from bs4 import BeautifulSoup
from requests import get

usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def _req(term, results, lang, start):
    resp = get(
        url="https://www.google.com/search",
        headers=usr_agent,
        params=dict(
            q = term,
            num = results + 2, # Prevents multiple requests
            hl = lang,
            start = start,
        )
    )
    resp.raise_for_status()
    return resp

class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"

def search(term):
    advanced=False
    lang="en"
    num_results=10
    escaped_term = term.replace(' ', '+')
    
    # Fetch
    start = 0
    while start < num_results:
        # Send request
        resp = _req(escaped_term, num_results-start, lang, start)

        # Parse
        soup = BeautifulSoup(resp.text, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            # Find link, title, description
            link = result.find('a', href=True)
            title = result.find('h3')
            description_box = result.find('div', {'style': '-webkit-line-clamp:2'})
            if description_box:
                description = description_box.find('span')
                if link and title and description:
                    start += 1
                    if advanced:
                        yield SearchResult(link['href'], title.text, description.text)
                    else:
                        yield link['href']

class GoogleE:
    def __init__(s, imports, logg):
        from googlesearch import search
        s.l = imports
        s.log = logg

        s.USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        s.headers = {"user-agent" : s.USER_AGENT}
    
    def search(s, q):
        q = str(q)
        
        s.log.fatal("You can find out the cause of the error or try to fix it by searching for the error in Google, here is one of the sites: " + str(list(search(q))[0]))
