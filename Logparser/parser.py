import re
from collections import Counter

def parse_log_file(file_path: str) -> dict:
    """
    Parses a log file and returns:
      - Count of each log level (ERROR, WARNING, INFO)
      - Top 3 most recurring full log messages

    :param file_path: path to the .log file
    :return: dict with 'levels' and 'top_messages'
    """
    pattern = re.compile(r"\b(ERROR|WARNING|INFO)\b")
    count_groups = Counter()
    message_counter = Counter()
    file_path = "instance/logs/sample.log"

    with open(file_path, "r", encoding="utf-8") as f:
        log_list = f.readlines()

    for line in log_list:
        match = pattern.search(line)
        if match:
            count_groups[match.group()] += 1
            message = line.strip()
            message_counter[message] += 1

    top_messages = message_counter.most_common(3)

    return {
        "levels": dict(count_groups),
        "top_messages": top_messages
    }

