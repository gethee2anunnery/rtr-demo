## RTR Shortlinks

This is a little prototype written in Django - it consists of a piece of middleware that catches 404s on a domain and routes them through a view controller which 1) generates and saves a row of data about the request and 2) redirects the browser to another specified URL.
