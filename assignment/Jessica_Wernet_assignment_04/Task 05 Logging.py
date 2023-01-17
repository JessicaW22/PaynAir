import logging 
import urllib.request

logging.basicConfig(level=logging.ERROR, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
                    
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
                
            
def open_url(url):
    
    try: 
        request_url = urllib.request.urlopen(url)
        content = request_url.read()
        string = content.decode("utf-8")
        
        print(string[:200])
        
    except Exception as e:
            logger.error(e)
            print(f"URL: {url}")
            
if __name__== "__main__":
    logger = init_log("mylog.txt", "w", "DEBUG", "message", "asctime")
    open_url(input("Write a website with www..."))