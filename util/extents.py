'''
This program checks extents(from starting point till ending point) of various
components of the program. Components include: functions, loops, conditionals,
structs, etc.
'''
import re

from store import counterparts, root
import parse
import utilities


possible_function_list = [
        'blank', 'comment1', 'preprocessor',
        'function_prototype', 'function_definition', 'forloop', 'whileloop',
        'dowhileloop', 'ifcondition', 'elseifcondition', 'elsecondition',
        'switch', 'declaration', 'assignment', 'struct', 'union'
]

def blank(lines_list, index):
    return index


def preprocessor(name, lines_list, index):
    '''
    Function returns index of the ending line of the preprocessor
    '''
    if index == len(lines_list): return index
    one_liners = ['define', 'include', 'line', 'pragma']
    #print name
    if name in one_liners:
        return index
    if parse.is_preprocessor(lines_list, index):
        thisname = re.search(r'\#(?P<name>\w+)', ).group('name')
        if thisname == counterparts[name]:
            return index
        thisend = preprocessor(thisname, lines_list, index)
        return preprocessor(name, lines_list, thisend+1)
    else:
        thisend = process_line(lines_list, index)
        return preprocessor(name, lines_list, thisend+1)


def function_prototype(lines_list, index):
    '''
    For now it handles only cases of the pattern:
    >>> rettype funcname(parameter_list);
    '''
    return index


def function_definition(lines_list, start_index, current_index, details={}):
    '''
    handles only function of the format
    >>> rettype func(args){
            body
        }
    '''
    if start_index == current_index:
        pattern = r'(?P<type>\w+)\s+(?P<name>\w+)\s*\((?P<args>.*)\)'
        # TODO: Put these details into dictionary

    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    statement_type = utilities.resolve(lines_list, index)
    returned = eval(statement_type +'(lines_list, index)')
    return function_definition(lines_list, returned+1)


def forloop(lines_list, index):
    '''
    handles only for loops of the format
    >>> for(details){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return forloop(lines_list, thisend+1)


def whileloop(lines_list, index):
    '''
    handles only while loops of the format
    >>> while(conditions){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return whileloop(lines_list, thisend+1)

def dowhileloop(lines_list, index):
    '''
    handles only dowhile loops of the format
    >>> do{
            body
        } while(condition);
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return dowhileloop(lines_list, thisend+1)

def ifcondition(lines_list, index):
    '''
    handles only if conditions of the format
    >>> if(conditions){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return ifcondition(lines_list, thisend+1)


def elseifcondition(lines_list, index):
    '''
    handles only else if conditions of the format
    >>> else if(conditions){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return elseifcondition(lines_list, thisend+1)


def elsecondition(lines_list, index):
    '''
    handles only else conditions of the format
    >>> else{
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return elsecondition(lines_list, thisend+1)


def switch(lines_list, index):
    '''
    handles only switch of the format
    >>> switch(constraint){
            body
        }
    '''
    if lines_list[index].strip() == '}':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return switch(lines_list, thisend+1)


def struct(lines_list, index):
    '''
    handles only structs of the format
    >>> struct name{
            body
        };
    '''
    if lines_list[index].strip() == '};':  #ignored inline comments for now
        return index
    thisend = process_line(lines_list, index)
    return struct(lines_list, thisend+1)

def union(lines_list, index):
    '''
    handles only structs of the format
    >>> union name{
            body
        };
    '''
    return index

def declaration(lines_list, index):
    '''handles only declarations of the following format
    >>> datatype var1;
    or
    >>> datatype var1, var2...;
    '''
    return index

def assignment(lines_list, index):
    '''handles only assignments of the following format
    >>> datatype var1 = val1;
    or any other inline assignment
    '''
    return index
