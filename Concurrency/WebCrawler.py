from typing import List
from queue import Queue
import threading

# Simple version
# Some worker may stop before handling all the new urls.
class Solution:
    def __init__(self):
        self.queue = Queue()
        self.lock = threading.Lock()

    def get_domain(self, url):
        return url.split('/')[2]

    def worker(self):
        while not self.queue.empty():
            url = self.queue.get()
            for new_url in self.htmlParser.getUrls(url):
                if self.get_domain(new_url) == self.domain:
                    if self.lock.acquire():
                        if new_url not in self.visited:
                            self.visited.add(new_url)
                            self.queue.put(new_url)
                        self.lock.release()
            self.queue.task_done()


    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:       
        self.visited = set([startUrl])
        self.domain = self.get_domain(startUrl)
        self.htmlParser = htmlParser

        N = 20
        workers = []
        self.queue.put(startUrl)
        
        for i in range(N):
            t = threading.Thread(target = self.worker)
            t.start()
            workers.append(t)

        self.queue.join()

        for t in workers:
            t.join()
        
        return list(self.visited)



# Faster version (use poison pill: put(None) to stop workers)
# Only need 8 workers now
from queue import Queue
import threading

class Solution:
    def __init__(self):
        self.queue = Queue()
        self.lock = threading.Lock()

    def get_domain(self, url):
        return url.split('/')[2]

    def worker(self):
        while True:
            url = self.queue.get()
            if not url:
                return

            for new_url in self.htmlParser.getUrls(url):
                if self.get_domain(new_url) == self.domain:
                    if self.lock.acquire():
                        if new_url not in self.visited:
                            self.visited.add(new_url)
                            self.queue.put(new_url)
                        self.lock.release()
            self.queue.task_done()


    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:       
        self.visited = set([startUrl])
        self.domain = self.get_domain(startUrl)
        self.htmlParser = htmlParser

        N = 8
        workers = []
        self.queue.put(startUrl)
        
        for i in range(N):
            t = threading.Thread(target = self.worker)
            t.start()
            workers.append(t)

        self.queue.join()

        for i in range(N):
            self.queue.put(None)

        for t in workers:
            t.join()
        
        return list(self.visited)