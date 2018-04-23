# This function will display consecutive "*" to indicate a loading screen.
# The amount of "*" and how long the load time is is indicated by the n value.
# For example; if you call loading(10) the program will display a new line of *, adding one * per line and waiting 1 second before displaying the next line, 10 times.

def loading(n):
        import time
        indicator = "*"
        loadTime = 0
        while loadTime != n:
                if loadTime == 0:
                        print(indicator)
                        loadTime = loadTime + 1
                        time.sleep(1)
                elif loadTime > 0 and loadTime != n:
                        print(indicator + "*")
                        indicator = indicator + "*"
                        loadTime = loadTime + 1
                        time.sleep(1)
                else:
                        loadTime = 0
                        indicator = "*"