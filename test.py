Test edition
2nd Test
3rd Test
c style search widget  
 2 +  
 3 +Translated from Tcl code by Schelte Bron, http://wiki.tcl.tk/18188  
 4 +"""  
 5 +import Tkinter  
 6 +import ttk  
 7 +  
 8 +root = Tkinter.Tk()  
 9 +  
 10 +data = """  
 11 +R0lGODlhKgAaAOfnAFdZVllbWFpcWVtdWlxeW11fXF9hXmBiX2ZnZWhpZ2lraGxua25wbXJ0  
 12 +cXR2c3V3dHZ4dXh6d3x+e31/fH6AfYSGg4eJhoiKh4qMiYuNio2PjHmUqnqVq3yXrZGTkJKU  
 13 +kX+asJSWk32cuJWXlIGcs5aYlX6euZeZloOetZial4SftpqbmIWgt4GhvYahuIKivpudmYei  
 14 +uYOjv5yem4ijuoSkwIWlwYmlu56gnYamwp+hnoenw4unvaCin4ioxJCnuZykrImpxZmlsoaq  
 15 +zI2pv6KkoZGouoqqxpqms4erzaOloo6qwYurx5Kqu5untIiszqSmo5CrwoysyJeqtpOrvJyo  
 16 +tZGsw42typSsvaaopZKtxJWtvp6qt4+uy6epppOuxZCvzKiqp5quuZSvxoyx06mrqJWwx42y  
 17 +1JKxzpmwwaqsqZaxyI6z1ZqxwqutqpOzz4+01qyuq56yvpizypS00Jm0y5W10Zq1zJa20rCy  
 18 +rpu3zqizwbGzr6C3yZy4z7K0saG4yp250LO1sqK5y5660Z+70qO7zKy4xaC806S8zba4taG9  
 19 +1KW9zq66x6+7yLi6t6S/1
