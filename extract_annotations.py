import json

start_page = 801
end_page = 877
f = open(f'testoutput-{start_page}-to-{end_page}.json')
data = json.load(f)

page_no = start_page

out_f = open(f'{start_page}-{end_page}.txt', 'w')
final_text = ''

for page in data['responses']:
    final_text += f"\n\n\n<<<{page_no}>>>\n\n\n"
    page_no += 1
    if 'fullTextAnnotation' not in page:
        continue
    text = page['fullTextAnnotation']['text']
    final_text += text

out_f.write(final_text)