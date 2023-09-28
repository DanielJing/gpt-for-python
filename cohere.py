import cohere
co = cohere.Client('{apiKey}')
response = co.generate(
  model='command-nightly',
  prompt='Write 5 titles for a blog ideas for the keywords \"large language model\" or \"text generation\"',
  max_tokens=300,
  temperature=0.9,
  k=0,
  p=0.75,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
