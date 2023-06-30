from elem import Elem, Text

class Html(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('html',content,attr,'double')
class Head(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('head',content,attr,'double')
class Body(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('body',content,attr,'double')
class Title(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('title',content,attr,'double')
class Meta(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('meta',content,attr,'simple')
class Img(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('img',content,attr,'simple')
class Table(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('table',content,attr,'double')
class Th(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('th',content,attr,'double')
class Tr(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('tr',content,attr,'double')
class Td(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('td',content,attr,'double')
class Ul(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('ul',content,attr,'double')
class Ol(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('ol',content,attr,'double')
class Li(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('li',content,attr,'double')
class H1(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('h1',content,attr,'double')
class H2(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('h2',content,attr,'double')
class P(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('p',content,attr,'double')
class Div(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('div',content,attr,'double')
class Span(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('span',content,attr,'double')
class Hr(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('hr',content,attr,'simple')
class Br(Elem):
    def __init__(self, content = None, attr={}):
        super().__init__('br',content,attr,'simple')

def mymain():
    print(Html([Head([Title([Text('"Hello ground!"')])]), Body([H1([Text('"Oh no, not again!"')]), Img(attr={'src': "http://i.imgur.com/pfp3T.jpg"})])]))

if __name__ == '__main__':
    mymain()