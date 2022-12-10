import json

start_page = 401
end_page = 414
path_prefix = 'bn-pandit/atmavilas'
f = open(f'{path_prefix}/raw/outputoutput-{start_page}-to-{end_page}.json')
data = json.load(f)

page_no = start_page

out_f = open(f'{path_prefix}/{start_page}-{end_page}.txt', 'w')
final_text = ''

for page in data['responses']:
    final_text += f"\n\n\n<<<{page_no}>>>\n\n\n"
    page_no += 1
    if 'fullTextAnnotation' not in page:
        continue
    text = page['fullTextAnnotation']['text']
    final_text += text

out_f.write(final_text)