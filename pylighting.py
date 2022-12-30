import tokenize

class Node:
    def __init__(self,prev_node,data,next_node) -> None:
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class Double_linked_list:
    def __init__(self,l:list) -> None:
        self.l = l
        self.start = None
        prev = None
        for idx,value in enumerate(l):
            if idx == 0:
                self.start = Node(None,value,None)
                prev = self.start
            else:
                prev.next_node = Node(prev,value,None)
                prev = prev.next_node
    def get_start(self):
        return self.start


def in_span(text ,clazz=None):
    if clazz is None:
        return f'<span>{text}</span>'
    return f'<span class={clazz}>{text}</span>'
    
def in_code(text):
    return f'<pre class="code_box"><code>{text}</code></pre>'



def highlight(path):
    str_class= "string"
    token_class= "token"
    func_class = "function"
    arg_class = "arg"
    parentheses_class = "parentheses"
    token_list = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 
    space = " "
    res = "\n"
    context = 0
    debth = 0
    with open(path, 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        ll = Double_linked_list(tokens)
        crnt = ll.get_start()
        while crnt is not None:
            token:token =  crnt.data
            debth += 1 if token[0] == 5 else -1 if token[0] == 6 else 0
            if len(res)>0 and res[-1] == '\n' and crnt.data[0] != 6 or crnt.prev_node is not None and crnt.prev_node.data[0] == 6 and crnt.data[0] != 6:
                #print(debth,token[:])
                #res += f'{debth}'
                res += debth * "\t"
            if token[0] in [5,6]:
                pass
            elif token[0] == 3:
                res+= in_span(token[1],str_class)
            elif token[0] == 1:
                if token[1] in token_list:
                    res+= in_span(token[1],token_class)
                elif crnt.next_node is not None and crnt.next_node.data[1] == '(' and crnt.prev_node is not None and crnt.prev_node.data[1] == 'def':
                    res += in_span(token[1],func_class)
                elif crnt.prev_node is not None and crnt.prev_node.data[1] == '@':
                    res += in_span(token[1],func_class)
                elif crnt.next_node is not None and crnt.next_node.data[1] == '=' and context > 0:
                    res += in_span(token[1],arg_class)
                else:
                    res += token[1]
            elif token[0] == 54:
                if token[1] in ['(',')','[',']','{','}']:
                    if token[1] == '(':
                        context += 1
                    elif token[1] == ')':
                        context -= 1
                    res += in_span(token[1],parentheses_class)
                elif token[1] == '@':
                    res += in_span(token[1],func_class)
                else:
                    res += token[1]
            elif token[0] == 62:
                pass
            else:
                res+= token[1]
            if crnt.next_node is not None and crnt.next_node.data[0] != 54 and token[1] not in ['.','(',':','@','\n','\r\n','{','['] and token[0] != 5 and token[0] != 6 or token[1] == 'import':
                res += space
            crnt = crnt.next_node  

    res+='\n'
    return in_code(res.strip())
    