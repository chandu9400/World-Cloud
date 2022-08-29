



# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import re


# Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed. 
# <br><br>
# **IMPORTANT!** If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above,  select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.
# <br><br>
# To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# In[13]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# Write a function in the cell below that iterates through the words in *file_contents*, removes punctuation, and counts the frequency of each word.  Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the".  Then use it in the `generate_from_frequencies` function to generate your very own word cloud!
# <br><br>
# **Hint:** Try storing the results of your iteration in a dictionary before passing them into wordcloud via the `generate_from_frequencies` function.

# In[22]:


def split_and_lower(file_contents):
    file_contents = file_contents.lower()
    array_words = file_contents.split()
    return array_words

def remove_non_alphabetic(source):
    new_array =[]
    #First parameter is the replacement, second parameter is your input string
    for word in source:
        regex = re.compile('[^a-zA-Z]')
        extra = regex.sub('', word)
        new_array.append(extra)
    return new_array


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    #punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    new_array = split_and_lower(file_contents)
    original_words = remove_non_alphabetic(new_array)
    
    for word in original_words:
        if word.isnumeric():
             original_words.remove(word)
    
    new_list = []
    new_dictionary = {}
    
    for word in original_words:
        if word not in new_dictionary:
            new_dictionary[word] = 1
        elif word in new_dictionary:
            new_dictionary[word] += 1
            
    for words in uninteresting_words:
        if words in new_dictionary:
            del new_dictionary[words]
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(new_dictionary)
    return cloud.to_array()
 


# If you have done everything correctly, your word cloud image should appear after running the cell below.  Fingers crossed!

# In[23]:


# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequecy count dictionary into the `generate_from_frequencies` function of `wordcloud`. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!





