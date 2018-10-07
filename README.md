# web-scraping-with-python
从bau网站按照指定word模板，在表格内填上公司、展位、国籍和网址信息。
bau网址https://exhibitors.bau-muenchen.com/en/

webcrawling.py
从bau网站爬取某个首字母的所有公司名称、展位、国籍信息。并且，从bing中获取，公司名称搜索结果的第一个网址（不全部可靠）作为公司网址。写到一个excel中。

excel-word.py
将上述excel内容，按指定模板，写入word文档表格中的指定位置，并按公司名称命名每个word。
