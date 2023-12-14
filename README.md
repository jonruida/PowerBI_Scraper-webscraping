These set of python scripts scrape the following:
1. The PDFs available at the website using selenium.
2. The content of the Power BI dashboard embedded on the webpage using requests (used the payload available at the Network>XHR component of the page to qurey the Power BI).

I want to thank the developer who created below script as it helped me understand the json content of the response and extract the appropriate fields.
- https://gist.github.com/svavassori/3319ff9d7e16a8788665ca59a5a04889
