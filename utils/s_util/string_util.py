from ..m_util.math_util import add     # . refers to relative import, which means import from the current package (utils)

def capitalize(str):
    if  len(str) <=1:
        return str.upper()

    return str[0].upper() + str[1:]

if __name__ == "__main__":
    print("string_util is running directly")