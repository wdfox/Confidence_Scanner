"""Script to Analyze Data"""

import os

import numpy as np
import pandas as pd

from consc.data import load_folder

from consc.analysis.sentiment import vader_doc, liu_polarity
from consc.analysis.subjectivity import doc_subjectivity
from consc.analysis.confidence import doc_confidence

###################################################################################################
###################################################################################################

DAT_PATH = '/Users/wdfox/Documents/GitCode/Confidence_Scanner/Data/'

DAT_TYPES = ['Papers', 'PRs']

# TERMS = ['autism', 'dementia', 'epilepsy', 'stroke', 'parkinsons', 'optogenetics', 'bilingualism', 'consciousness', 'perception', 'cognition', 'vaccines', 'coma', 'diabetes', 'hypertension']
TERMS = ['autism', 'dementia']

###################################################################################################
###################################################################################################

def main():

	for dat_type in DAT_TYPES:

		print('Running ', dat_type)

		# Initialize dataframe
		df = pd.DataFrame(columns=['id', 'vader', 'liu', 'subj', 'liwc'])

		for term in TERMS:

			print('\tRunning ', term)

			# Load the data
			docs = load_folder(dat_type, term, DAT_PATH, proc_text=True)
			print('Loaded')

			for ind, doc in enumerate(docs):

				# Skip any documents that have no text
				if not doc.text:
					continue

				# Calculate readability measures
				vader = vader_doc(doc)
				liu = liu_polarity(doc)
				subj = doc_subjectivity(doc)
				liwc = doc_confidence(doc)

				# Append to dataframe
				df = df.append({'term' : term,
								'vader' : vader,
								'liu' : liu,
								'subj' : subj,
								'liwc' : liwc
								}, ignore_index=True)

				print('\t', ind, 'out of', len(docs))

		df.to_csv(os.path.join('results', dat_type + '_analysis.csv'))


if __name__ == '__main__':
	main()

