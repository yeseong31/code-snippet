import csv
import gzip


def process_gz_read_write(args):
    target_file_path, save_file_path = args

    with gzip.open(target_file_path, mode='rt', encoding='utf-8') as infile, \
            gzip.open(save_file_path, mode='wt', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter='|')
        writer = csv.writer(outfile, delimiter='|')
        total_record_count = 0

        for row in reader:
            writer.writerow(row)
            total_record_count += 1

        if total_record_count == 0:
            save_file_path.unlink()
            return 0

        # 레코드 건수 기록
        writer.writerow([total_record_count])

    return total_record_count
