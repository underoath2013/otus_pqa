import os
import re
import json


def process_log_file(file_path) -> dict:
    # Открытие и парсинг лог-файла
    with open(file_path, 'r') as file:
        print(f"Processing file: {file_path}")

        log_data = file.readlines()

        pattern = r'(?P<remote_host>\S+) - - \[(?P<timestamp>.*?)\] "(?P<http_method>\S+) (?P<request>.*?)" (?P<http_status>\d+) (?P<bytes_sent>\d+) "(?P<referer>.*?)" "(?P<user_agent>.*?)" (?P<request_duration>\d+)'

        total_requests = 0
        http_method_counts = {}
        ip_counts = {}
        longest_requests = []  # список словарей

        for line in log_data:
            item = re.match(pattern, line)
            if item:
                total_requests += 1

                http_method = item.group('http_method')
                http_method_counts[http_method] = http_method_counts.get(http_method, 0) + 1

                remote_host = item.group('remote_host')
                ip_counts[remote_host] = ip_counts.get(remote_host, 0) + 1

                request_duration = int(item.group('request_duration'))
                request_info = {
                    'method': http_method,
                    'url': item.group('request'),
                    'ip': remote_host,
                    'duration': request_duration,
                    'timestamp': item.group('timestamp')
                }
                longest_requests.append(request_info)

        top_3_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        top_3_longest_requests = sorted(longest_requests, key=lambda x: x['duration'], reverse=True)[:3]

        print(f"Total requests {total_requests}")
        print(f"Http method: counts {http_method_counts}")
        print(f"Top 3 ip's: counts {top_3_ips}")
        print(f"Top 3 longest requests {top_3_longest_requests}")
        print("="*40)

        # Возвращаем результаты анализа для данного файла
        return {
            "filename": os.path.basename(file_path),
            "total_requests": total_requests,
            "http_method_counts": http_method_counts,
            "top_ip_addresses": top_3_ips,
            "top_longest_requests": top_3_longest_requests
        }


def process_logs_in_directory(directory_path) -> list:
    all_output_data = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.log'):
                file_path = os.path.join(root, file)
                output_data = process_log_file(file_path)
                all_output_data.append(output_data)

    return all_output_data


def save_result_to_json(all_output_data):
    output_file_path = "output.json"
    with open(output_file_path, "w") as output_file:
        json.dump(all_output_data, output_file, indent=4)

    print(f"Output saved to {output_file_path}")


def main():
    path = input("Введите путь к директории или файлу логов: ")
    path = os.path.normpath(path)

    if os.path.isdir(path):
        save_result_to_json(process_logs_in_directory(path))
    elif os.path.isfile(path) and path.endswith('.log'):
        save_result_to_json(process_log_file(path))
    else:
        print("Некорректный путь или файл")


if __name__ == "__main__":
    main()
