from HTMLParser import HTMLParser
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.checkbox_list = []
        self.checkbox_data_list = []
        self.textInput_list = []
        self.textInput_data_list = []
        self.tr_start = []
        self.tr_end = []        
        
        self.input_type = None
        
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'input':
            for name, value in attrs:
                if name == 'type' and value == 'checkbox':                      # Find checkbox tag input and add it to an array
                    self.checkbox_list.append(attrs[0])
                    self.input_type = 'checkbox'
                elif name == 'type' and value == 'text':                        # Find text field tag and add it to an array
                    self.textInput_list.append(attrs[0])
                    self.input_type = 'text input'
        elif tag.lower() == 'tr':                                               # Find "tr" tag and start recording. 
            print self.getpos()
            self.tr_start.append(self.getpos())
            
    def handle_endtag(self, tag):
        if tag.lower() == 'tr':                                                 # Find "/tr' tag and stop recording. Recorded html will then be parsed.
            print self.getpos()
            self.tr_end.append(self.getpos())
            
        
    def handle_data(self, data):
        if self.input_type == 'checkbox':
            self.checkbox_data_list.append(data)    
        elif self.input_type == 'text input':
            self.textInput_data_list.append(data)
            
        self.input_type = None                          

#    def date_input(self):
        

    def get_data(self):
        checkbox_ids = []
        textInput_ids = []
        for name, value in self.checkbox_list:
            checkbox_ids.append(value)
        for name, value in self.textInput_list:
            textInput_ids.append(value)
            
        checkbox_info = zip(checkbox_ids, self.checkbox_data_list)
        
#        textInput_info = zip(textInput_ids, self.textInput_data_list)          
        
        return checkbox_info

class 

def DataCollector(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.get_data()

url = 'https://rdcrnqa.epi.usf.edu//rdnwebapp/Forms/05VCRC/5532/RecurringMedications.aspx?EventScheduleId=12658&RdcrnProtocolId=5532&ProtocolId=363&creguid=1697&trimester=4'
page = urllib2.urlopen(url)
html = page.read()

req = urllib2.Request('https://rdcrnqa.epi.usf.edu//rdnwebapp/Forms/05VCRC/5532/RecurringMedications.aspx?EventScheduleId=12658&RdcrnProtocolId=5532&ProtocolId=363&creguid=1697&trimester=4')
response = urllib2.urlopen(req)

lines = "" 
for x in range(1446, 1449):
        lines += response.readline(x)        
print(lines)

print DataCollector(html)


