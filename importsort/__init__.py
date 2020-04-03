#!/usr/bin/env python3
"""
Sorts imports at the top of a file.
"""

import argparse
from pathlib import Path

import toml
from bowler import Query, TOKEN
from fissix.pygram import python_symbols as syms


STDLIB_MODULES_PY37 = '__future__,__phello__,_abc,_ast,_asyncio,_bisect,_blake2,_bootlocale,_bz2,_codecs,_codecs_cn,_codecs_hk,_codecs_iso2022,_codecs_jp,_codecs_kr,_codecs_tw,_collections,_collections_abc,_compat_pickle,_compression,_contextvars,_crypt,_csv,_ctypes,_ctypes_test,_curses,_curses_panel,_datetime,_dbm,_decimal,_dummy_thread,_elementtree,_functools,_gdbm,_hashlib,_heapq,_imp,_io,_json,_locale,_lsprof,_lzma,_markupbase,_md5,_multibytecodec,_multiprocessing,_opcode,_operator,_osx_support,_pickle,_posixsubprocess,_py_abc,_pydecimal,_pyio,_queue,_random,_scproxy,_sha1,_sha256,_sha3,_sha512,_signal,_sitebuiltins,_socket,_sqlite3,_sre,_ssl,_stat,_string,_strptime,_struct,_symtable,_sysconfigdata_m_darwin_darwin,_testbuffer,_testcapi,_testimportmultiple,_testmultiphase,_thread,_threading_local,_tkinter,_tracemalloc,_uuid,_warnings,_weakref,_weakrefset,_xxtestfuzz,abc,aifc,antigravity,argparse,array,ast,asynchat,asyncio,asyncore,atexit,audioop,base64,bdb,binascii,binhex,bisect,builtins,bz2,cProfile,calendar,cgi,cgitb,chunk,cmath,cmd,code,codecs,codeop,collections,colorsys,compileall,concurrent,config-3,configparser,contextlib,contextvars,copy,copyreg,crypt,csv,ctypes,curses,dataclasses,datetime,dbm,decimal,difflib,dis,distutils,doctest,dummy_threading,email,encodings,ensurepip,enum,errno,faulthandler,fcntl,filecmp,fileinput,fnmatch,formatter,fractions,ftplib,functools,gc,genericpath,getopt,getpass,gettext,glob,grp,gzip,hashlib,heapq,hmac,html,http,idlelib,imaplib,imghdr,imp,importlib,inspect,io,ipaddress,itertools,json,keyword,lib2to3,linecache,locale,logging,lzma,macpath,mailbox,mailcap,marshal,math,mimetypes,mmap,modulefinder,multiprocessing,netrc,nis,nntplib,ntpath,nturl2path,numbers,opcode,operator,optparse,os,parser,pathlib,pdb,pickle,pickletools,pipes,pkgutil,platform,plistlib,poplib,posix,posixpath,pprint,profile,pstats,pty,pwd,py_compile,pyclbr,pydoc,pydoc_data,pyexpat,queue,quopri,random,re,readline,reprlib,resource,rlcompleter,runpy,sched,secrets,select,selectors,shelve,shlex,shutil,signal,site,smtpd,smtplib,sndhdr,socket,socketserver,sqlite3,sre_compile,sre_constants,sre_parse,ssl,stat,statistics,string,stringprep,struct,subprocess,sunau,symbol,symtable,sys,sysconfig,syslog,tabnanny,tarfile,telnetlib,tempfile,termios,test,textwrap,this,threading,time,timeit,tkinter,token,tokenize,trace,traceback,tracemalloc,tty,turtle,turtledemo,types,typing,unicodedata,unittest,urllib,uu,uuid,venv,warnings,wave,weakref,webbrowser,wsgiref,xdrlib,xml,xmlrpc,xxlimited,xxsubtype,zipapp,zipfile,zipimport,zli'  # noqa
STDLIB_MODULES_PY27 = u'BaseHTTPServer,Bastion,CGIHTTPServer,ColorPicker,ConfigParser,Cookie,DocXMLRPCServer,HTMLParser,MacOS,MimeWriter,Nav,OSATerminology,Queue,SimpleHTTPServer,SimpleXMLRPCServer,SocketServer,StringIO,UserDict,UserList,UserString,_AE,_AH,_App,_CF,_CG,_CarbonEvt,_Cm,_Ctl,_Dlg,_Drag,_Evt,_File,_Fm,_Folder,_Help,_IBCarbon,_Icn,_LWPCookieJar,_Launch,_List,_Menu,_Mlte,_MozillaCookieJar,_OSA,_Qd,_Qdoffs,_Res,_Scrap,_Snd,_TE,_Win,__builtin__,__future__,__main__,__phello__,_abcoll,_ast,_bisect,_codecs,_codecs_cn,_codecs_hk,_codecs_iso2022,_codecs_jp,_codecs_kr,_codecs_tw,_collections,_csv,_ctypes,_ctypes_test,_curses,_curses_panel,_elementtree,_functools,_hashlib,_heapq,_hotshot,_io,_json,_locale,_lsprof,_multibytecodec,_multiprocessing,_osx_support,_pyio,_random,_scproxy,_socket,_sqlite3,_sre,_ssl,_strptime,_struct,_symtable,_sysconfigdata,_testcapi,_threading_local,_tkinter,_warnings,_weakref,_weakrefset,abc,aifc,antigravity,anydbm,argparse,array,ast,asynchat,asyncore,atexit,audiodev,audioop,autoGIL,base64,bdb,binascii,binhex,bisect,bsddb,bsddb185,bz2,cPickle,cProfile,cStringIO,calendar,cgi,cgitb,chunk,cmath,cmd,code,codecs,codeop,collections,colorsys,commands,compileall,compiler,contextlib,cookielib,copy,copy_reg,crypt,csv,ctypes,curses,datetime,dbhash,dbm,decimal,difflib,dircache,dis,distutils,doctest,dumbdbm,dummy_thread,dummy_threading,email,encodings,ensurepip,errno,exceptions,fcntl,filecmp,fileinput,fnmatch,formatter,fpformat,fractions,ftplib,functools,future_builtins,gc,gdbm,genericpath,gestalt,getopt,getpass,gettext,glob,grp,gzip,hashlib,heapq,hmac,hotshot,htmlentitydefs,htmllib,httplib,icglue,idlelib,ihooks,imaplib,imghdr,imp,importlib,imputil,inspect,io,itertools,json,keyword,lib-tk,lib2to3,linecache,locale,logging,macpath,macurl2path,mailbox,mailcap,markupbase,marshal,math,md5,mhlib,mimetools,mimetypes,mimify,mmap,modulefinder,multifile,multiprocessing,mutex,netrc,new,nis,nntplib,ntpath,nturl2path,numbers,opcode,operator,optparse,os,os2emxpath,parser,pdb,pickle,pickletools,pipes,pkgutil,plat-darwin,plat-mac,platform,plistlib,popen2,poplib,posix,posixfile,posixpath,pprint,profile,pstats,pty,pwd,py_compile,pyclbr,pydoc,pydoc_data,pyexpat,quopri,random,re,readline,repr,resource,rexec,rfc822,rlcompleter,robotparser,runpy,sched,select,sets,sgmllib,sha,shelve,shlex,shutil,signal,site,smtpd,smtplib,sndhdr,socket,sqlite3,sre,sre_compile,sre_constants,sre_parse,ssl,stat,statvfs,string,stringold,stringprep,strop,struct,subprocess,sunau,sunaudio,symbol,symtable,sys,sysconfig,syslog,tabnanny,tarfile,telnetlib,tempfile,termios,test,textwrap,this,thread,threading,time,timeit,toaiff,token,tokenize,trace,traceback,tty,types,unicodedata,unittest,urllib,urllib2,urlparse,user,uu,uuid,warnings,wave,weakref,webbrowser,whichdb,wsgiref,xdrlib,xml,xmllib,xmlrpclib,xxsubtype,zipfile,zipimport,zlib'  # noqa

STDLIB_MODULES = set(STDLIB_MODULES_PY37.split(',') + STDLIB_MODULES_PY27.split(','))


class SkipString(ValueError):
    pass


def get_top_import_nodes(file_node):
    """
    Returns all nodes from the top of the file,
    up to (but not including) the first non-import node.
    """
    import_allowed_nodes = []
    for node in file_node.children:
        if node.type != syms.simple_stmt:
            return import_allowed_nodes
        imp = node.children[0]
        if imp.type not in (
            TOKEN.STRING,
            TOKEN.NEWLINE,
            syms.import_from,
            syms.import_name,
        ):
            # something else? terminate the top-of-file imports here.
            return import_allowed_nodes
        import_allowed_nodes.append(imp)


cfg = None


def init_cfg():
    global cfg
    path = Path('~/.importsort.cfg').expanduser()
    if path.exists():
        with path.open() as f:
            cfg = toml.load(f)
    else:
        cfg = {}
    # Set defaults.
    cfg.setdefault('first_party_modules', [])
    cfg['first_party_modules'] = set(cfg['first_party_modules'])


def _sort_imported_names(parent_node):
    """
    Given a syms.import_as_names node,
    re-orders the child nodes (imported names) so that they are sorted alphabetically.
    Returns the name of the first imported name, after sorting.
    """
    orig_nodes = []
    sorted_nodes = []
    for n in parent_node.children:
        if n.type in (TOKEN.NAME, syms.import_as_name):
            orig_nodes.append(n)
            sorted_nodes.append(n.clone())

    def get_name(n):
        return n.value if n.type == TOKEN.NAME else n.children[0].value

    sorted_nodes.sort(key=get_name)

    for orig, new in zip(orig_nodes, sorted_nodes):
        orig.replace(new)

    return get_name(sorted_nodes[0])


COMMENT_SPLITTER = '!!IMPORTSORT!!'


def sort_imports(root, capture, filename):
    import_nodes = get_top_import_nodes(root)
    module_imports = []

    # * Go through all top-of-file imports.
    # * Index them by module name.
    # * Do inline sorting of imported names (`import b, c, a` --> `import a, b, c`)
    for imp in import_nodes:
        first_name = None
        if imp.next_sibling:
            # detach any end-of-line comment and store it for later.
            # this associates it with the import itself.
            comment = imp.next_sibling.prefix.lstrip()
            if comment.startswith('#'):
                # comment on the same line as imp.
                imp.next_sibling.prefix = '\n'
                # hack: move the comment into the prefix of `imp` so it stays with imp
                # when we sort.
                # We'll move it onto the next sibling node again after sorting.
                # So that we keep track of which comments to move, append a suffix to the comment
                # so we notice.
                imp.prefix = f'{imp.prefix}{COMMENT_SPLITTER}  {comment}\n'
        if imp.type == syms.import_name:
            module_node = imp.children[1]
            if module_node.type == TOKEN.NAME:
                # 'import os'
                module = module_node.value
            elif module_node.type == syms.dotted_name:
                # 'import x.y'
                module = str(module_node)
            elif module_node.type == syms.dotted_as_name:
                # 'import os as OS'
                module = module_node.children[0].value
            elif module_node.type == syms.dotted_as_names:
                # 'import os, io'
                module = _sort_imported_names(imp.children[1])

            else:
                raise ValueError(f"Unknown import format: {imp}")
        elif imp.type == syms.import_from:
            module_node = imp.children[1]
            if module_node.type == syms.dotted_name:
                # 'from x.y import z'
                module = str(module_node.children[0])
            else:
                module = module_node.value
            names = [n for n in imp.children[3:] if n.type != TOKEN.LPAR]
            if names[0].type == TOKEN.NAME:
                # 'from x import y'
                first_name = names[0].value
            elif names[0].type == syms.import_as_name:
                # 'from x import y as z'
                first_name = names[0].children[0].value
            elif names[0].type == syms.import_as_names:
                # 'from x import y, z'
                # 'from x import y as a, z as b'
                first_name = _sort_imported_names(names[0])
            else:
                raise ValueError(f"Unknown import format: {imp}")
        elif imp.type == syms.NEWLINE:
            imp.remove()
        else:
            # top-of-module docstring. float to top.
            module = ''

        root_module_name = module.split('.')[0]

        # do 'from ...' imports after 'import ...' imports.
        from_ = 1 if first_name is not None else 0

        if root_module_name == '':
            # module docstring
            group = 0
        elif root_module_name == '__future__':
            # special case; must come first
            group = 1
        elif root_module_name in STDLIB_MODULES:
            # stdlib modules
            group = 2
        elif root_module_name not in cfg['first_party_modules']:
            # third party modules
            group = 3
        else:
            # first party modules
            group = 4
        module_imports.append((group, from_, module, first_name, imp.clone()))

    # Now sort the various lines we've encountered.
    module_imports.sort()

    # Now, clear out all the statements from the parse tree
    for n in import_nodes:
        n.parent.remove()

    # Then repopulate the tree with the sorted nodes, cleaning up whitespace as we go.
    last_group = 0
    next_prefix_comment = None
    for i, (group, from_, module, first_name, node) in enumerate(module_imports):
        prefix = node.prefix
        if last_group != group:
            # add a space between groups.
            prefix = f'\n\n{prefix.lstrip()}'
        if next_prefix_comment:
            prefix = f'{next_prefix_comment}{prefix}'
            next_prefix_comment = None
        if COMMENT_SPLITTER in prefix:
            prefix, next_prefix_comment = prefix.split(COMMENT_SPLITTER, 1)
        if i == 0:
            prefix = prefix.lstrip()
        node.prefix = prefix
        root.insert_child(i, node)
        last_group = group

    try:
        next_child = root.children[i + 1]
        print(f'nc {next_child!r}')
    except IndexError:
        pass
    else:
        next_child.prefix = (
            f'{next_prefix_comment or ""}\n\n\n{next_child.prefix.lstrip()}'
        )


def main():
    parser = argparse.ArgumentParser(description="Sorts top-of-file imports.")
    parser.add_argument(
        '--no-write',
        dest='write',
        default=True,
        action='store_false',
        help="Don't write the changes to the source file, just output a diff to stdout",
    )
    parser.add_argument(
        'files', nargs='+', help="The python source file(s) to operate on."
    )
    args = parser.parse_args()
    init_cfg()

    (
        # Look for files in the current working directory
        Query(*args.files)
        .select_root()
        .modify(callback=sort_imports)
        # Actually run both of the above.
        .execute(
            # interactive diff implies write (for the bits the user says 'y' to)
            interactive=False,
            write=args.write,
        )
    )
