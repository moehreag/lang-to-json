import json
import argparse
 
def main():

    json_string = "{\n"

    parser = argparse.ArgumentParser(description="Convert .lang files to json, or format json files!")
    parser.add_argument('-i', '--input', help='The file to convert (when ending in .lang)/format')

    args = parser.parse_args()

    if ".lang" in args.input:
        f = open(args.input, "r")

        for line in f.readlines():
            if("=" in line):
                s = line.strip().replace('"', '\\\"').split("=", 1)
                json_string += '\n"axolotlclient.'+s[0]+'": "'+s[1]+'",'
            else:
                json_string += "\n"

        json_string = json_string[:-1]
        json_string += '\n}'

        f.close()

        new_file = args.input.split(".lang")[0].lower()+".json"
        #open(new_file, "x")
        jf = open(new_file, "w")

        jf.write(json.dumps(json.loads(json_string), sort_keys=True, indent=4))

        jf.close()

    else:
        jf = open(args.input, 'r')

        #json_string = jf.read().replace("\n", "")

        #jf.close()

        json_string = ""
        for line in jf.readlines():
            if(len(line)>0):
                json_string += line.strip()

        #print(json_string)

        jf.close()

        jf = open(args.input, 'w')

        #jf.write(json_string)

        json_serialized = json.loads(json_string)
        jf.write(json.dumps(json_serialized, sort_keys=True, indent=4))

        jf.close()

if __name__ == '__main__':
    main()
