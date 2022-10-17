import json
import argparse
 
def main():

    json_string = "{\n"

    parser = argparse.ArgumentParser(description="Convert .lang files to json!")
    parser.add_argument('-i', '--input', help='The file to convert')

    args = parser.parse_args()

    f = open(args.input, "r")

    for line in f.readlines():
        if("=" in line):
            s = line.strip().replace('"', '\\\"').split("=", 1)
            json_string += '\n"'+s[0]+'": "'+s[1]+'",'
        else:
            json_string += "\n"

    json_string = json_string[:-1]
    json_string += '\n}'

    f.close()

    new_file = args.input.split(".lang")[0]+".json"
    open(new_file, "x")
    jf = open(new_file, "w")

    jf.write(json.dumps(json.loads(json_string), indent=4))

    jf.close()

if __name__ == '__main__':
    main()
