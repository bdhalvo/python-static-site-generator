import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)


    def load(self, cls, string):
        _, fm, content = __regex.split(string, depth=2)
        
        load(fm, Loader=FullLoader)
        return cls(metadata, content)


    @property
    def body(self):
        return self.data["content"]


    @property
    def type(self):
        return self.data["type"] if self.data["type"] else None


    def set_type(self, new_type)
        self.data["type"] = new_type


    def __init__(self, metadata, content):
        data = metadata
        self.data = "content": content


    def __getitem__(self, key):
        return self.data[key]

    
    def __iter__(self):
        return self.data.iter()


    def __len__(self):
        return len(self.data)

    
    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value

        return str(data)