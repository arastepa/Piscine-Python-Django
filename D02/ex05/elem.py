#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    # [...]
    class ValidationError(Exception):
        def __init__(self):
            super().__init__('behaviour not expected')


    def __init__(self, tag='div', content=None, attr = {}, tag_type='double'):
        self.tag = tag
        self.content = []
        self.attr = attr
        self.tag_type = tag_type
        if content is not None:
            self.add_content(content)
    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        myattr  = self.__make_attr()
        result = '<{tag}{attr}'.format(tag = self.tag, attr = myattr)
        if self.tag_type == 'double':
            result += '>{content}</{tag}>'.format(content = self.__make_content(),tag = self.tag)
        elif self.tag_type == 'simple':
            result += '/>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += '  ' + str(elem).replace('\n', '\n  ')
            result += '\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
def myElem():
    # print (str(Elem(tag='body', attr={}, content=Elem())))
    print(str(Elem(content = Elem(content=Elem()))))

if __name__ == '__main__':
    myElem()
