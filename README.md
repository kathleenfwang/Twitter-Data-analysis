# Twitter-Data-analysis

Sentiment analyzer for real-time tweets. Displays a percentage for positive, negative, and neutral tweets. 

##  Functionality: 

- Retrieves tweets based on a user inputted string
- Uses a sentiment analyzer library to detect percentage of positive,negative, and neutral tweets
- Checks tweets against a pre-defined list of words that are deemed positive or negative 


## Three steps to run: 
- Obtain your Twitter API and Tokens from the [Twitter developer website](https://developer.twitter.com/en.html)
- Update the token and key variables: 
```sh
consumer_key = '<YOUR KEY>'
consumer_secret = '<YOUR SECRET>'
access_token = '<ACCESS TOKEN>'
access_token_secret = '<TOKEN SECRET>'

```
- Clone the file locally: 
```sh
git clone https://github.com/kathleenfwang/twitter-data-analsys.git
```
- Install dependencies: 
```sh
pip install -r requirements.txt
```
- Run main.py!
```sh
python main.py
```
