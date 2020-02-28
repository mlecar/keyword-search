import requests
import json
import configparser


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    keyword_service_url = config['default']['keyword_service_url']
    source_file = config['default']['source_file']
    target_file = config['default']['target_file']
    body = config['default']['body']

    file_results = open(target_file, 'w')

    keywords_list = []

    with open(source_file, "r") as f:
        lines = f.read().splitlines()
        for x in lines:
            keywords_list.append(x.strip())

    n = 100 # each 100 keywords
    final = [keywords_list[i * n:(i + 1) * n] for i in range((len(keywords_list) + n - 1) // n)]

    for x in final:
        body_keywords = ""
        for y in x:
            body_keywords += "&keyword[]=" + y

        r = requests.get(keyword_service_url, str(body) + body_keywords)
        result = r.text.encode("utf-8")
        print(result)
        json_obj = json.loads(result, "utf-8")
        # print(json_obj)
        for y in json_obj["response"]:
            keyword_id = y["keyword_id"]
            keyword = y["keyword"]
            # print(str(keyword_id) + " - " + keyword)
            if keyword_id is None:
                file_results.write(keyword.encode("utf-8") + ";null;\n")
            else:
                file_results.write(keyword.encode("utf-8") + ";" + str(keyword_id) + ";\n")
        r.close()


if __name__ == "__main__":
    main()
