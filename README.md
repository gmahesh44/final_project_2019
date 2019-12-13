Project on HIV/AIDS prevalence in world and in general in US

I am working addressing the HIV transmission with patients treated with antiretroviral therapy. The research showed that new infections resulted when the partner living with HIV was not fully virally suppressed due to either having just started antiretroviral therapy, or for whom treatment no longer was working and the virus was replicating. Thus it is advisable that prevention is better than cure. In this direction I was curious to know the prevalence of HIV in the world population and in general US population. In this direction, I was able to find the data from WHO (https://www.who.int/hiv/data/en/). As mentioned on the website the most prevalent in Africa, then South-East Asia and followed by Americas, Europe etc.

My goal here is to find which country in the world is most prevalent with AIDS and which one is highest in Americas.

To address this:
1. I will get the data from the above mentioned site in a csv format
2. Upload the file using pandas
3. Data selected for the countries and 
4. Display in graph using seaborn

Reading CSV Data file:
I used pandas to upload the CSV file using pd.read_csv() function. To preserve the original file, I generated another file df = data. Using df file checked how many data is in file and found 680 information from all the countries.

Selecting the resective file for further analysis:
Using the df file generated df1 file to further select only the columns that needs to be analyzed. Removed all the data that does not contain any information (NaN). 

Data analysis and plots:
Data was plotted using seaborn and matplotlib. The data shows that Africa has more incidence compared to other parts of the world. Just for clarification I tried to compare which country in Africa has more HIV cases. Since it is difficult to know which countries has more incidence I selected the population which has more than 1000000 incidences (df1[df1['Numeric']>1000000]). As the data shows the ZAF referred as South Africa has higher incidence of HIV cases compared to all the other african countries. Next I wanted to check which countries have higher incidence and from which continent I know I can write a loop function but I used alternative way to create new file. Then I used df1[df1['Numeric']<1000000] and by creating another file df3[df3['Numeric']>700000] which has the population infected with HIV between 700000 to 1000000. The above result suggests that in 2010 USA comes under the highest incidence catagory compared to all the other nations. Since the data for 2018 is not available fot USA this might have crossed the incidence level of second category and might have been in the first category

Conclusion:
In conlusion, as I mentioned before that eventhough the antiviral therapy is effective the HIV prevalence is higher in US and until further progress in research up until complete suppression is achieved it is better to be precautious and take necessary steps in preventing the disease.

References:

1. https://www.who.int/hiv/data/en/
