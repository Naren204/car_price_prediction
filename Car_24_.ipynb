{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:27:17.390641Z",
     "start_time": "2021-03-27T07:27:07.361450Z"
    }
   },
   "outputs": [],
   "source": [
    "# Visualizations lib\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.ticker as mtick \n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "pd.options.display.max_rows = 100\n",
    "\n",
    "# models\n",
    "from sklearn.impute import KNNImputer \n",
    "from sklearn.ensemble import ExtraTreesRegressor\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_squared_error\n",
    "import pickle\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "# from jupyterthemes import jtplot\n",
    "# jtplot.style()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "headers = {\n",
    "    'authority': 'api-sell24.cars24.team',\n",
    "    'accept': 'application/json, text/plain, */*',\n",
    "    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',\n",
    "    'pincode': '110001',\n",
    "    'origin': 'https://www.cars24.com',\n",
    "    'sec-fetch-site': 'cross-site',\n",
    "    'sec-fetch-mode': 'cors',\n",
    "    'sec-fetch-dest': 'empty',\n",
    "    'referer': 'https://www.cars24.com/',\n",
    "    'accept-language': 'en-US,en;q=0.9',\n",
    "}\n",
    "\n",
    "params = (\n",
    "    ('sort', 'P'),\n",
    "    ('serveWarrantyCount', 'false'),\n",
    "    ('gaId', '332617789.1611807407'),\n",
    "    ('page', '3'),\n",
    "    ('storeCityId', '2'),\n",
    ")\n",
    "\n",
    "response = requests.get('https://api-sell24.cars24.team/buy-used-car', headers=headers, params=params)\n",
    "\n",
    "totalPages = response.json()['data']['totalPages'] \n",
    "# print(totalPages)\n",
    "\n",
    "link_list = []\n",
    "\n",
    "for i in range(totalPages):\n",
    "    url = 'https://www.cars24.com/buy-used-car/?sort=P&page=' + str(i+1) + '&storeCityId=2'\n",
    "# url = 'https://www.cars24.com/buy-used-car/?sort=P&page=4&storeCityId=2'\n",
    "# Step 1 : Get the HTML\n",
    "    r = requests.get(url)\n",
    "    htmlContent = r.content\n",
    "# print(htmlContent)\n",
    "\n",
    "\n",
    "# Step 2 : Parse the html\n",
    "    soup = BeautifulSoup(htmlContent,\"html.parser\")\n",
    "\n",
    "    for link in soup.find_all('a', href=True, class_ = '_20d39'):\n",
    "        link_list.append(link['href'])\n",
    "\n",
    "\n",
    "print(link_list)\n",
    "\n",
    "# Get all the paragraphs from the page\n",
    "paras = soup.find_all('p')\n",
    "# print(paras)\n",
    "\n",
    "# Get all the anchor tags from the page\n",
    "anchors = soup.find_all('a')\n",
    "# print(anchors)\n",
    "\n",
    "#get all the links on the page\n",
    "all_links = set()\n",
    "for link in anchors:\n",
    "    if (link != '#'):\n",
    "        all_links.add(link.get('href'))\n",
    "# print(all_links)\n",
    "\n",
    "for link in soup.find_all('a', class_ = \"\"):\n",
    "    \n",
    "    if(link.get_text()==\"Next\"):\n",
    "        url = 'https://www.cars24.com/buy-used-cars-new-delhi/' + link['href']\n",
    "# Step 1 : Get the HTML\n",
    "        r = requests.get(url)\n",
    "        htmlContent = r.content\n",
    "# print(htmlContent)\n",
    "\n",
    "# Step 2 : Parse the html\n",
    "        sp = BeautifulSoup(htmlContent,'html.parser')\n",
    "    # if (link == '#'):\n",
    "    #     print('hello')\n",
    "        # for link in soup.find_all('a', href=True, class_ = '_20d39'):\n",
    "        #     print(link['href'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fill_data(ca,c1):\n",
    "    if ca == \"Kilometers\":\n",
    "        km_ = c1.find('p').getText()\n",
    "        km.append(km_) \n",
    "    elif ca == \"Year of Purchase\":\n",
    "        year_ = c1.find('p').getText()\n",
    "        year.append(year_)\n",
    "    elif ca == 'Owner':\n",
    "        owner_type_ = c1.find('p').getText()\n",
    "        owner_type.append(owner_type_)\n",
    "    elif ca == 'Fuel':\n",
    "        fuel_type_ = c1.find('p').getText()\n",
    "        fuel_type.append(fuel_type_)\n",
    "    elif ca == 'Transmission':\n",
    "        transmission_type_ = c1.find('p').getText()\n",
    "        transmission_type.append(transmission_type_)\n",
    "    elif ca == 'RTO':\n",
    "        RTO_ = c1.find('p').getText()\n",
    "        RTO.append(RTO_)\n",
    "    elif ca == 'Insurance Type':\n",
    "        insurance_type_ = c1.find('p').getText()\n",
    "        insurance_type.append(insurance_type_)\n",
    "    elif ca == 'Insurance':\n",
    "        insurance_date_ = c1.find('p').getText()\n",
    "        insurance_date.append(insurance_date_)    \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def len_list(a):\n",
    "    if len(km)!=a:\n",
    "        km.append('NA')\n",
    "    elif len(year)!=a:\n",
    "        year.append('NA')\n",
    "    elif len(owner_type)!=a:\n",
    "        owner_type.append('NA')\n",
    "    elif len(fuel_type)!=a:\n",
    "        fuel_type.append('NA')\n",
    "    elif len(insurance_type)!=a:\n",
    "        insurance_type.append('NA')\n",
    "    elif len(insurance_date)!=a:\n",
    "        insurance_date.append('NA')\n",
    "    elif len(transmission_type)!=a:\n",
    "        transmission_type.append('NA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "km = []\n",
    "car_model = []\n",
    "year = []\n",
    "owner_type = []\n",
    "fuel_type = []\n",
    "transmission_type = []\n",
    "RTO = []\n",
    "insurance_type = []\n",
    "insurance_date = []\n",
    "price = []\n",
    "n = 0\n",
    "for i in range(len(link_list)):\n",
    "    page = requests.get(link_list[i])\n",
    "    soup = BeautifulSoup(page.text, 'html.parser')\n",
    "    c1 = soup.find_all('div',{'class':'col-3'})\n",
    "    if not c1:\n",
    "        n = n + 1\n",
    "        continue\n",
    "    car_model_ = soup.find_all('div',{'class':'col-4'})[0]\n",
    "    car_model_= car_model_.find('p').getText()#[5:17]\n",
    "    car_model.append(car_model_)\n",
    "    price_ = soup.find_all('div',{'class':'col-4'})[0]\n",
    "    price_ = price_.find('h4').getText()\n",
    "    price.append(price_)\n",
    "    \n",
    "    c0=soup.find_all('div',{'class':'col-3'})[0]\n",
    "    l0=c0.find('label').getText()\n",
    "    fill_data(l0,c0)\n",
    "    \n",
    "    c1=soup.find_all('div',{'class':'col-3'})[1]\n",
    "    l1=c1.find('label').getText()\n",
    "    fill_data(l1,c1)\n",
    "    \n",
    "    c2=soup.find_all('div',{'class':'col-3'})[2]\n",
    "    l2=c2.find('label').getText()\n",
    "    fill_data(l2,c2)\n",
    "    \n",
    "    c3=soup.find_all('div',{'class':'col-3'})[3]\n",
    "    l3=c3.find('label').getText()\n",
    "    fill_data(l3,c3)\n",
    "    \n",
    "    c4=soup.find_all('div',{'class':'col-3'})[4]\n",
    "    l4=c4.find('label')\n",
    "    if l4==None:\n",
    "        continue\n",
    "    else:\n",
    "        l4=l4.getText()\n",
    "    fill_data(l4,c4)\n",
    "    \n",
    "    c5=soup.find_all('div',{'class':'col-3'})[5]\n",
    "    l5=c5.find('label')\n",
    "    if l5==None:\n",
    "        continue\n",
    "    else:\n",
    "        l5=l5.getText()\n",
    "    fill_data(l5,c5)\n",
    "    \n",
    "    c6=soup.find_all('div',{'class':'col-3'})[6]\n",
    "    l6=c6.find('label')\n",
    "    if l6==None:\n",
    "        continue\n",
    "    else:\n",
    "        l6=l6.getText()\n",
    "    fill_data(l6,c6)\n",
    "    \n",
    "    c7=soup.find_all('div',{'class':'col-3'})[7]\n",
    "    l7=c7.find('label')\n",
    "    if l7==None:\n",
    "        continue\n",
    "    else:\n",
    "        l7=l7.getText()\n",
    "    fill_data(l7,c7)\n",
    "    \n",
    "    len_list(i+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(list(zip(km, car_model,year,owner_type,insurance_date,insurance_type,RTO,fuel_type,transmission_type,price)), \n",
    "    columns =['Kilometers', 'cars_model','Year','Owner_Type','Insurance_Date','Insurance_Type','RTO','Fuel_Type','Transmission_Type','Price']) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# save to csv\n",
    "df.to_csv('car24_Delhi_records.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:30.817416Z",
     "start_time": "2021-03-27T07:33:30.782861Z"
    }
   },
   "outputs": [],
   "source": [
    "# read the data\n",
    "df = pd.read_csv('car24_Delhi_records.csv')\n",
    "data = pd.DataFrame()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Kilometers</th>\n",
       "      <th>cars_model</th>\n",
       "      <th>Year</th>\n",
       "      <th>Owner_Type</th>\n",
       "      <th>Insurance_Date</th>\n",
       "      <th>Insurance_Type</th>\n",
       "      <th>RTO</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Transmission_Type</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50,007 km</td>\n",
       "      <td>2014 Tata Nano XT TWIST</td>\n",
       "      <td>December 2014</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>22/2/2021</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL11</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>₹ 114,899</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>19,577 km</td>\n",
       "      <td>2016 Maruti Celerio ZXI OPT AMT</td>\n",
       "      <td>April 2016</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>10/5/2021</td>\n",
       "      <td>Zero_Dep</td>\n",
       "      <td>DL6C</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>₹ 368,499</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>57,650 km</td>\n",
       "      <td>2011 Maruti Wagon R 1.0 LXI CNG</td>\n",
       "      <td>May 2011</td>\n",
       "      <td>Second Owner</td>\n",
       "      <td>20/9/2021</td>\n",
       "      <td>Third_party</td>\n",
       "      <td>DL8C</td>\n",
       "      <td>Petrol + CNG</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>₹ 196,199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47,447 km</td>\n",
       "      <td>2010 Hyundai Santro Xing GLS</td>\n",
       "      <td>March 2010</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>27/3/2021</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL3C</td>\n",
       "      <td>Petrol + CNG</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>₹ 156,460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>13,337 km</td>\n",
       "      <td>2016 Maruti Alto K10 LXI</td>\n",
       "      <td>May 2016</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>2/11/2021</td>\n",
       "      <td>Expired</td>\n",
       "      <td>DL6C</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>₹ 293,447</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Kilometers                       cars_model           Year    Owner_Type  \\\n",
       "0  50,007 km          2014 Tata Nano XT TWIST  December 2014   First Owner   \n",
       "1  19,577 km  2016 Maruti Celerio ZXI OPT AMT     April 2016   First Owner   \n",
       "2  57,650 km  2011 Maruti Wagon R 1.0 LXI CNG       May 2011  Second Owner   \n",
       "3  47,447 km     2010 Hyundai Santro Xing GLS     March 2010   First Owner   \n",
       "4  13,337 km         2016 Maruti Alto K10 LXI       May 2016   First Owner   \n",
       "\n",
       "  Insurance_Date Insurance_Type   RTO     Fuel_Type Transmission_Type  \\\n",
       "0      22/2/2021           Comp  DL11        Petrol            MANUAL   \n",
       "1      10/5/2021       Zero_Dep  DL6C        Petrol         AUTOMATIC   \n",
       "2      20/9/2021    Third_party  DL8C  Petrol + CNG            MANUAL   \n",
       "3      27/3/2021           Comp  DL3C  Petrol + CNG            MANUAL   \n",
       "4      2/11/2021        Expired  DL6C        Petrol            MANUAL   \n",
       "\n",
       "       Price  \n",
       "0  ₹ 114,899  \n",
       "1  ₹ 368,499  \n",
       "2  ₹ 196,199  \n",
       "3  ₹ 156,460  \n",
       "4  ₹ 293,447  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:32.499904Z",
     "start_time": "2021-03-27T07:33:32.285224Z"
    }
   },
   "outputs": [],
   "source": [
    "# feature engineering\n",
    "\n",
    "data1 = [] \n",
    "data2 = []\n",
    "data3 = []\n",
    "for i in range(0,len(df)):\n",
    "    model  = df['cars_model'][i][5:-1]\n",
    "    data1.append(model)\n",
    "    brand = ' '.join(df['cars_model'][i][5:-1].split()[:1])\n",
    "    data2.append(brand)\n",
    "    car_model = ' '.join(df['cars_model'][i][5:-1].split()[1:2])\n",
    "    data3.append(car_model)\n",
    "\n",
    "data['Car_model'] = data1\n",
    "data['Brand_name'] = data2\n",
    "#data['Model_name'] = data3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:33.910648Z",
     "start_time": "2021-03-27T07:33:33.796292Z"
    }
   },
   "outputs": [],
   "source": [
    "df['Year'][1] = df.Year.str.split(\" \",n=-1,expand=True)\n",
    "data['Year'] = df['Year'][1][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:34.101955Z",
     "start_time": "2021-03-27T07:33:34.023194Z"
    }
   },
   "outputs": [],
   "source": [
    "df['Kilometers'][1] = df.Kilometers.str.split(\" \",n=-1,expand=True)\n",
    "data['Kilometers'] = df['Kilometers'][1][0]\n",
    "data['Kilometers'] = data['Kilometers'].str.replace(',','')\n",
    "data[\"Kilometers\"] = pd.to_numeric(data[\"Kilometers\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:34.251073Z",
     "start_time": "2021-03-27T07:33:34.236218Z"
    }
   },
   "outputs": [],
   "source": [
    "data['Fuel_Type'] = df['Fuel_Type']\n",
    "data['Owner_Type'] = df['Owner_Type']\n",
    "data['Insurance_Type'] = df['Insurance_Type']\n",
    "data['RTO'] = df['RTO']\n",
    "data['Transmission_Type'] = df['Transmission_Type']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:34.523559Z",
     "start_time": "2021-03-27T07:33:34.448284Z"
    }
   },
   "outputs": [],
   "source": [
    "df['Price'][1] = df.Price.str.split(\" \", n=-1, expand=True)\n",
    "data['Price'] = df['Price'][1][1]\n",
    "data['Price'] = data['Price'].str.replace(',','')\n",
    "data[\"Price\"] = pd.to_numeric(data[\"Price\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:34.585126Z",
     "start_time": "2021-03-27T07:33:34.561099Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2378 entries, 0 to 2377\n",
      "Data columns (total 10 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Car_model          2378 non-null   object \n",
      " 1   Brand_name         2378 non-null   object \n",
      " 2   Year               2357 non-null   object \n",
      " 3   Kilometers         2357 non-null   float64\n",
      " 4   Fuel_Type          2357 non-null   object \n",
      " 5   Owner_Type         2357 non-null   object \n",
      " 6   Insurance_Type     2359 non-null   object \n",
      " 7   RTO                2378 non-null   object \n",
      " 8   Transmission_Type  2225 non-null   object \n",
      " 9   Price              2378 non-null   int64  \n",
      "dtypes: float64(1), int64(1), object(8)\n",
      "memory usage: 185.9+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:34.773980Z",
     "start_time": "2021-03-27T07:33:34.762478Z"
    }
   },
   "outputs": [],
   "source": [
    "# # data['No. of years'] = data.apply(lambda x:2021-int(x))\n",
    "# data.drop(['Car_model','Year'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:35.035366Z",
     "start_time": "2021-03-27T07:33:34.988971Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Car_model</th>\n",
       "      <th>Brand_name</th>\n",
       "      <th>Year</th>\n",
       "      <th>Kilometers</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Owner_Type</th>\n",
       "      <th>Insurance_Type</th>\n",
       "      <th>RTO</th>\n",
       "      <th>Transmission_Type</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Tata Nano XT TWIS</td>\n",
       "      <td>Tata</td>\n",
       "      <td>2014</td>\n",
       "      <td>50007.0</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL11</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>114899</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Maruti Celerio ZXI OPT AM</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2016</td>\n",
       "      <td>19577.0</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>Zero_Dep</td>\n",
       "      <td>DL6C</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>368499</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Maruti Wagon R 1.0 LXI CN</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2011</td>\n",
       "      <td>57650.0</td>\n",
       "      <td>Petrol + CNG</td>\n",
       "      <td>Second Owner</td>\n",
       "      <td>Third_party</td>\n",
       "      <td>DL8C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>196199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hyundai Santro Xing GL</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2010</td>\n",
       "      <td>47447.0</td>\n",
       "      <td>Petrol + CNG</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL3C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>156460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Maruti Alto K10 LX</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2016</td>\n",
       "      <td>13337.0</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>Expired</td>\n",
       "      <td>DL6C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>293447</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Maruti Alto K10 LX</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2011</td>\n",
       "      <td>32089.0</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Second Owner</td>\n",
       "      <td>Third_party</td>\n",
       "      <td>DL3C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>173699</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Maruti Alto 800 LX</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2013</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL9C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>203081</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Maruti Ritz VDI</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>NaN</td>\n",
       "      <td>28769.0</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>First Owner</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL9C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>300199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Maruti Celerio ZXI AM</td>\n",
       "      <td>Maruti</td>\n",
       "      <td>2012</td>\n",
       "      <td>16061.0</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL9C</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>399804</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Hyundai i10 MAGNA 1.1 IRDE</td>\n",
       "      <td>Hyundai</td>\n",
       "      <td>2018</td>\n",
       "      <td>18002.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Second Owner</td>\n",
       "      <td>Comp</td>\n",
       "      <td>DL2C</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>172600</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Car_model Brand_name  Year  Kilometers     Fuel_Type  \\\n",
       "0           Tata Nano XT TWIS       Tata  2014     50007.0        Petrol   \n",
       "1   Maruti Celerio ZXI OPT AM     Maruti  2016     19577.0        Petrol   \n",
       "2   Maruti Wagon R 1.0 LXI CN     Maruti  2011     57650.0  Petrol + CNG   \n",
       "3      Hyundai Santro Xing GL    Hyundai  2010     47447.0  Petrol + CNG   \n",
       "4          Maruti Alto K10 LX     Maruti  2016     13337.0        Petrol   \n",
       "5          Maruti Alto K10 LX     Maruti  2011     32089.0        Petrol   \n",
       "6          Maruti Alto 800 LX     Maruti  2013         NaN        Petrol   \n",
       "7             Maruti Ritz VDI     Maruti   NaN     28769.0        Diesel   \n",
       "8       Maruti Celerio ZXI AM     Maruti  2012     16061.0        Petrol   \n",
       "9  Hyundai i10 MAGNA 1.1 IRDE    Hyundai  2018     18002.0           NaN   \n",
       "\n",
       "     Owner_Type Insurance_Type   RTO Transmission_Type   Price  \n",
       "0   First Owner           Comp  DL11            MANUAL  114899  \n",
       "1   First Owner       Zero_Dep  DL6C         AUTOMATIC  368499  \n",
       "2  Second Owner    Third_party  DL8C            MANUAL  196199  \n",
       "3   First Owner           Comp  DL3C            MANUAL  156460  \n",
       "4   First Owner        Expired  DL6C            MANUAL  293447  \n",
       "5  Second Owner    Third_party  DL3C            MANUAL  173699  \n",
       "6   First Owner           Comp  DL9C            MANUAL  203081  \n",
       "7   First Owner           Comp  DL9C            MANUAL  300199  \n",
       "8           NaN           Comp  DL9C         AUTOMATIC  399804  \n",
       "9  Second Owner           Comp  DL2C            MANUAL  172600  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:35.136246Z",
     "start_time": "2021-03-27T07:33:35.132616Z"
    }
   },
   "outputs": [],
   "source": [
    "# data['Model_name'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:35.717305Z",
     "start_time": "2021-03-27T07:33:35.706482Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Car_model              0\n",
       "Brand_name             0\n",
       "Year                  21\n",
       "Kilometers            21\n",
       "Fuel_Type             21\n",
       "Owner_Type            21\n",
       "Insurance_Type        19\n",
       "RTO                    0\n",
       "Transmission_Type    153\n",
       "Price                  0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:36.840749Z",
     "start_time": "2021-03-27T07:33:35.929386Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Percentage of missing values per feature')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Percentage of missing values per feature\n",
    "data.isna().sum()\n",
    "ax = (data.isnull().mean() * 100).plot(kind='bar', color ='orange')\n",
    "ax.yaxis.set_major_formatter(mtick.PercentFormatter())\n",
    "plt.title('Percentage of missing values per feature')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:36.857249Z",
     "start_time": "2021-03-27T07:33:36.845225Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Comp', 'Zero_Dep', 'Third_party', 'Expired', nan,\n",
       "       'Insurance Expired', 'Comprehensive', 'Zero Depreciation',\n",
       "       '3rd Party'], dtype=object)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# unique values\n",
    "data['Insurance_Type'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:36.928809Z",
     "start_time": "2021-03-27T07:33:36.906480Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['2014', '2016', '2011', '2010', '2013', nan, '2012', '2018',\n",
       "       '2017', '2019', '2015', '2008', '2020', '2009', '2007', '2006',\n",
       "       '2005', '2002'], dtype=object)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:37.721808Z",
     "start_time": "2021-03-27T07:33:37.716284Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Petrol', 'Petrol + CNG', 'Diesel', nan, 'Petrol + LPG',\n",
       "       'Electric'], dtype=object)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Fuel_Type'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:38.409213Z",
     "start_time": "2021-03-27T07:33:38.396537Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Petrol          1435\n",
       "Diesel           620\n",
       "Petrol + CNG     299\n",
       "Petrol + LPG       2\n",
       "Electric           1\n",
       "Name: Fuel_Type, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Fuel_Type'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:39.034901Z",
     "start_time": "2021-03-27T07:33:38.997234Z"
    }
   },
   "outputs": [],
   "source": [
    "data.loc[data['Fuel_Type']=='Electric','Fuel_Type'] = 'Petrol'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:39.407643Z",
     "start_time": "2021-03-27T07:33:39.393654Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Petrol', 'Petrol + CNG', 'Diesel', nan, 'Petrol + LPG'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Fuel_Type'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:40.550703Z",
     "start_time": "2021-03-27T07:33:40.536491Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['First Owner', 'Second Owner', nan, 'Third Owner', 'Fourth Owner',\n",
       "       'Sixth Owner'], dtype=object)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Owner_Type'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:41.005122Z",
     "start_time": "2021-03-27T07:33:40.993177Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['MANUAL', 'AUTOMATIC', nan], dtype=object)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Transmission_Type'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:41.679127Z",
     "start_time": "2021-03-27T07:33:41.669587Z"
    }
   },
   "outputs": [],
   "source": [
    "# fig = plt.figure(figsize=(25, 15))\n",
    "# cols = 5\n",
    "# rows = np.ceil(float(data.shape[1]) / cols)\n",
    "\n",
    "# for i, column in enumerate(data.columns):\n",
    "#     ax = fig.add_subplot(rows, cols, i + 1)\n",
    "#     ax.set_title(column)\n",
    "#     if data.dtypes[column] == np.object:\n",
    "#         data[column].value_counts().plot(kind=\"bar\", axes=ax)\n",
    "#     else:\n",
    "#         data[column].hist(axes=ax)\n",
    "#         plt.xticks(rotation=\"vertical\")\n",
    "# plt.subplots_adjust(hspace=0.7, wspace=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:42.112100Z",
     "start_time": "2021-03-27T07:33:42.096196Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2378 entries, 0 to 2377\n",
      "Data columns (total 10 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   Car_model          2378 non-null   object \n",
      " 1   Brand_name         2378 non-null   object \n",
      " 2   Year               2357 non-null   object \n",
      " 3   Kilometers         2357 non-null   float64\n",
      " 4   Fuel_Type          2357 non-null   object \n",
      " 5   Owner_Type         2357 non-null   object \n",
      " 6   Insurance_Type     2359 non-null   object \n",
      " 7   RTO                2378 non-null   object \n",
      " 8   Transmission_Type  2225 non-null   object \n",
      " 9   Price              2378 non-null   int64  \n",
      "dtypes: float64(1), int64(1), object(8)\n",
      "memory usage: 185.9+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:42.519741Z",
     "start_time": "2021-03-27T07:33:42.512805Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Car_model', 'Brand_name', 'Year', 'Kilometers', 'Fuel_Type',\n",
       "       'Owner_Type', 'Insurance_Type', 'RTO', 'Transmission_Type', 'Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:33:43.339617Z",
     "start_time": "2021-03-27T07:33:43.323122Z"
    }
   },
   "outputs": [],
   "source": [
    "# separate features on basis of their types\n",
    "num_v = data.select_dtypes(['int64','float'])\n",
    "cat_v = data.select_dtypes(['O'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:02.808271Z",
     "start_time": "2021-03-27T07:34:02.798948Z"
    }
   },
   "outputs": [],
   "source": [
    "# fill missing values for numerical features\n",
    "imputer = KNNImputer() \n",
    "num_v_1 = imputer.fit_transform(num_v) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:05.352034Z",
     "start_time": "2021-03-27T07:34:05.341454Z"
    }
   },
   "outputs": [],
   "source": [
    "numerical_df = pd.DataFrame(num_v_1,columns=list(num_v.columns))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:06.073076Z",
     "start_time": "2021-03-27T07:34:06.035570Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Kilometers</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50007.0</td>\n",
       "      <td>114899.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>19577.0</td>\n",
       "      <td>368499.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>57650.0</td>\n",
       "      <td>196199.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47447.0</td>\n",
       "      <td>156460.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>13337.0</td>\n",
       "      <td>293447.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2373</th>\n",
       "      <td>4640.0</td>\n",
       "      <td>200000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2374</th>\n",
       "      <td>56245.0</td>\n",
       "      <td>415000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2375</th>\n",
       "      <td>43850.0</td>\n",
       "      <td>1850000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2376</th>\n",
       "      <td>83470.0</td>\n",
       "      <td>280000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2377</th>\n",
       "      <td>16640.0</td>\n",
       "      <td>131495.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2378 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Kilometers      Price\n",
       "0        50007.0   114899.0\n",
       "1        19577.0   368499.0\n",
       "2        57650.0   196199.0\n",
       "3        47447.0   156460.0\n",
       "4        13337.0   293447.0\n",
       "...          ...        ...\n",
       "2373      4640.0   200000.0\n",
       "2374     56245.0   415000.0\n",
       "2375     43850.0  1850000.0\n",
       "2376     83470.0   280000.0\n",
       "2377     16640.0   131495.0\n",
       "\n",
       "[2378 rows x 2 columns]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numerical_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:14.266539Z",
     "start_time": "2021-03-27T07:34:14.260989Z"
    }
   },
   "outputs": [],
   "source": [
    "numerical_df['Kilometers'] = np.log10(numerical_df['Kilometers'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:15.171178Z",
     "start_time": "2021-03-27T07:34:15.156886Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    2012\n",
       "dtype: object"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v['Year'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:15.432697Z",
     "start_time": "2021-03-27T07:34:15.421494Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Petrol\n",
       "dtype: object"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v['Fuel_Type'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:15.673025Z",
     "start_time": "2021-03-27T07:34:15.659463Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    First Owner\n",
       "dtype: object"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v['Owner_Type'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:15.940349Z",
     "start_time": "2021-03-27T07:34:15.928700Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Comp\n",
       "dtype: object"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v['Insurance_Type'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:16.374690Z",
     "start_time": "2021-03-27T07:34:16.365192Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    MANUAL\n",
       "dtype: object"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v['Transmission_Type'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:17.118442Z",
     "start_time": "2021-03-27T07:34:16.875286Z"
    }
   },
   "outputs": [],
   "source": [
    "# fill missing values of categorical values\n",
    "\n",
    "cat_v[\"Year\"].fillna('2012', inplace = True)  \n",
    "cat_v[\"Fuel_Type\"].fillna('Petrol', inplace = True)  \n",
    "cat_v[\"Owner_Type\"].fillna('Fifth Owner', inplace = True)  \n",
    "cat_v[\"Insurance_Type\"].fillna('Comp', inplace = True) \n",
    "cat_v[\"Transmission_Type\"].fillna('MANUAL', inplace = True) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:17.280138Z",
     "start_time": "2021-03-27T07:34:17.263284Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Car_model            0\n",
       "Brand_name           0\n",
       "Year                 0\n",
       "Fuel_Type            0\n",
       "Owner_Type           0\n",
       "Insurance_Type       0\n",
       "RTO                  0\n",
       "Transmission_Type    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:17.994052Z",
     "start_time": "2021-03-27T07:34:17.846513Z"
    }
   },
   "outputs": [],
   "source": [
    "cat_v['Year'] = cat_v['Year'].astype('int64')\n",
    "cat_v['Years'] = cat_v['Year'].apply(lambda x:2021-x)\n",
    "cat_v.drop(['Car_model','Year'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:18.153222Z",
     "start_time": "2021-03-27T07:34:18.099200Z"
    }
   },
   "outputs": [],
   "source": [
    "cat_v['RTO']=cat_v['RTO'].apply(lambda x:'Delhi'if x.startswith(\"DL\") else 'Other_State')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:18.401766Z",
     "start_time": "2021-03-27T07:34:18.372116Z"
    }
   },
   "outputs": [],
   "source": [
    "cat_v = pd.get_dummies(cat_v, drop_first=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:19.198299Z",
     "start_time": "2021-03-27T07:34:19.028194Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Years</th>\n",
       "      <th>Brand_name_BMW</th>\n",
       "      <th>Brand_name_Chevrolet</th>\n",
       "      <th>Brand_name_Datsun</th>\n",
       "      <th>Brand_name_Fiat</th>\n",
       "      <th>Brand_name_Ford</th>\n",
       "      <th>Brand_name_Honda</th>\n",
       "      <th>Brand_name_Hyundai</th>\n",
       "      <th>Brand_name_Jeep</th>\n",
       "      <th>Brand_name_KIA</th>\n",
       "      <th>...</th>\n",
       "      <th>Owner_Type_Third Owner</th>\n",
       "      <th>Insurance_Type_Comp</th>\n",
       "      <th>Insurance_Type_Comprehensive</th>\n",
       "      <th>Insurance_Type_Expired</th>\n",
       "      <th>Insurance_Type_Insurance Expired</th>\n",
       "      <th>Insurance_Type_Third_party</th>\n",
       "      <th>Insurance_Type_Zero Depreciation</th>\n",
       "      <th>Insurance_Type_Zero_Dep</th>\n",
       "      <th>RTO_Other_State</th>\n",
       "      <th>Transmission_Type_MANUAL</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2373</th>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2374</th>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2375</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2376</th>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2377</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2378 rows × 39 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Years  Brand_name_BMW  Brand_name_Chevrolet  Brand_name_Datsun  \\\n",
       "0         7               0                     0                  0   \n",
       "1         5               0                     0                  0   \n",
       "2        10               0                     0                  0   \n",
       "3        11               0                     0                  0   \n",
       "4         5               0                     0                  0   \n",
       "...     ...             ...                   ...                ...   \n",
       "2373      6               0                     0                  0   \n",
       "2374     11               0                     0                  0   \n",
       "2375      5               0                     0                  0   \n",
       "2376     10               0                     0                  0   \n",
       "2377      2               0                     0                  0   \n",
       "\n",
       "      Brand_name_Fiat  Brand_name_Ford  Brand_name_Honda  Brand_name_Hyundai  \\\n",
       "0                   0                0                 0                   0   \n",
       "1                   0                0                 0                   0   \n",
       "2                   0                0                 0                   0   \n",
       "3                   0                0                 0                   1   \n",
       "4                   0                0                 0                   0   \n",
       "...               ...              ...               ...                 ...   \n",
       "2373                0                0                 0                   1   \n",
       "2374                0                0                 0                   0   \n",
       "2375                0                0                 0                   0   \n",
       "2376                0                0                 0                   0   \n",
       "2377                0                0                 0                   1   \n",
       "\n",
       "      Brand_name_Jeep  Brand_name_KIA  ...  Owner_Type_Third Owner  \\\n",
       "0                   0               0  ...                       0   \n",
       "1                   0               0  ...                       0   \n",
       "2                   0               0  ...                       0   \n",
       "3                   0               0  ...                       0   \n",
       "4                   0               0  ...                       0   \n",
       "...               ...             ...  ...                     ...   \n",
       "2373                0               0  ...                       0   \n",
       "2374                0               0  ...                       0   \n",
       "2375                1               0  ...                       0   \n",
       "2376                0               0  ...                       0   \n",
       "2377                0               0  ...                       0   \n",
       "\n",
       "      Insurance_Type_Comp  Insurance_Type_Comprehensive  \\\n",
       "0                       1                             0   \n",
       "1                       0                             0   \n",
       "2                       0                             0   \n",
       "3                       1                             0   \n",
       "4                       0                             0   \n",
       "...                   ...                           ...   \n",
       "2373                    0                             1   \n",
       "2374                    0                             0   \n",
       "2375                    0                             0   \n",
       "2376                    1                             0   \n",
       "2377                    0                             0   \n",
       "\n",
       "      Insurance_Type_Expired  Insurance_Type_Insurance Expired  \\\n",
       "0                          0                                 0   \n",
       "1                          0                                 0   \n",
       "2                          0                                 0   \n",
       "3                          0                                 0   \n",
       "4                          1                                 0   \n",
       "...                      ...                               ...   \n",
       "2373                       0                                 0   \n",
       "2374                       0                                 0   \n",
       "2375                       0                                 0   \n",
       "2376                       0                                 0   \n",
       "2377                       0                                 0   \n",
       "\n",
       "      Insurance_Type_Third_party  Insurance_Type_Zero Depreciation  \\\n",
       "0                              0                                 0   \n",
       "1                              0                                 0   \n",
       "2                              1                                 0   \n",
       "3                              0                                 0   \n",
       "4                              0                                 0   \n",
       "...                          ...                               ...   \n",
       "2373                           0                                 0   \n",
       "2374                           0                                 0   \n",
       "2375                           0                                 1   \n",
       "2376                           0                                 0   \n",
       "2377                           0                                 0   \n",
       "\n",
       "      Insurance_Type_Zero_Dep  RTO_Other_State  Transmission_Type_MANUAL  \n",
       "0                           0                0                         1  \n",
       "1                           1                0                         0  \n",
       "2                           0                0                         1  \n",
       "3                           0                0                         1  \n",
       "4                           0                0                         1  \n",
       "...                       ...              ...                       ...  \n",
       "2373                        0                0                         1  \n",
       "2374                        1                0                         1  \n",
       "2375                        0                0                         1  \n",
       "2376                        0                0                         1  \n",
       "2377                        0                0                         1  \n",
       "\n",
       "[2378 rows x 39 columns]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:20.210536Z",
     "start_time": "2021-03-27T07:34:20.204694Z"
    }
   },
   "outputs": [],
   "source": [
    "bn = data['Brand_name'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:20.524608Z",
     "start_time": "2021-03-27T07:34:20.514561Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Tata', 'Maruti', 'Hyundai', 'Datsun', 'Honda', 'Toyota', 'Ford',\n",
       "       'Renault', 'Volkswagen', 'Mahindra', 'BMW', 'Mercedes', 'Skoda',\n",
       "       'Chevrolet', 'Nissan', 'Fiat', 'KIA', 'Ssangyong', 'MG', 'Audi',\n",
       "       'Volvo', 'Jeep'], dtype=object)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:20.781903Z",
     "start_time": "2021-03-27T07:34:20.766627Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Years', 'Brand_name_BMW', 'Brand_name_Chevrolet', 'Brand_name_Datsun',\n",
       "       'Brand_name_Fiat', 'Brand_name_Ford', 'Brand_name_Honda',\n",
       "       'Brand_name_Hyundai', 'Brand_name_Jeep', 'Brand_name_KIA',\n",
       "       'Brand_name_MG', 'Brand_name_Mahindra', 'Brand_name_Maruti',\n",
       "       'Brand_name_Mercedes', 'Brand_name_Nissan', 'Brand_name_Renault',\n",
       "       'Brand_name_Skoda', 'Brand_name_Ssangyong', 'Brand_name_Tata',\n",
       "       'Brand_name_Toyota', 'Brand_name_Volkswagen', 'Brand_name_Volvo',\n",
       "       'Fuel_Type_Petrol', 'Fuel_Type_Petrol + CNG', 'Fuel_Type_Petrol + LPG',\n",
       "       'Owner_Type_First Owner', 'Owner_Type_Fourth Owner',\n",
       "       'Owner_Type_Second Owner', 'Owner_Type_Sixth Owner',\n",
       "       'Owner_Type_Third Owner', 'Insurance_Type_Comp',\n",
       "       'Insurance_Type_Comprehensive', 'Insurance_Type_Expired',\n",
       "       'Insurance_Type_Insurance Expired', 'Insurance_Type_Third_party',\n",
       "       'Insurance_Type_Zero Depreciation', 'Insurance_Type_Zero_Dep',\n",
       "       'RTO_Other_State', 'Transmission_Type_MANUAL'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:21.220095Z",
     "start_time": "2021-03-27T07:34:21.088599Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Brand_name_BMW</th>\n",
       "      <th>Brand_name_Chevrolet</th>\n",
       "      <th>Brand_name_Datsun</th>\n",
       "      <th>Brand_name_Fiat</th>\n",
       "      <th>Brand_name_Ford</th>\n",
       "      <th>Brand_name_Honda</th>\n",
       "      <th>Brand_name_Hyundai</th>\n",
       "      <th>Brand_name_Jeep</th>\n",
       "      <th>Brand_name_KIA</th>\n",
       "      <th>Brand_name_MG</th>\n",
       "      <th>...</th>\n",
       "      <th>Brand_name_Maruti</th>\n",
       "      <th>Brand_name_Mercedes</th>\n",
       "      <th>Brand_name_Nissan</th>\n",
       "      <th>Brand_name_Renault</th>\n",
       "      <th>Brand_name_Skoda</th>\n",
       "      <th>Brand_name_Ssangyong</th>\n",
       "      <th>Brand_name_Tata</th>\n",
       "      <th>Brand_name_Toyota</th>\n",
       "      <th>Brand_name_Volkswagen</th>\n",
       "      <th>Brand_name_Volvo</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2373</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2374</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2375</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2376</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2377</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2378 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Brand_name_BMW  Brand_name_Chevrolet  Brand_name_Datsun  \\\n",
       "0                  0                     0                  0   \n",
       "1                  0                     0                  0   \n",
       "2                  0                     0                  0   \n",
       "3                  0                     0                  0   \n",
       "4                  0                     0                  0   \n",
       "...              ...                   ...                ...   \n",
       "2373               0                     0                  0   \n",
       "2374               0                     0                  0   \n",
       "2375               0                     0                  0   \n",
       "2376               0                     0                  0   \n",
       "2377               0                     0                  0   \n",
       "\n",
       "      Brand_name_Fiat  Brand_name_Ford  Brand_name_Honda  Brand_name_Hyundai  \\\n",
       "0                   0                0                 0                   0   \n",
       "1                   0                0                 0                   0   \n",
       "2                   0                0                 0                   0   \n",
       "3                   0                0                 0                   1   \n",
       "4                   0                0                 0                   0   \n",
       "...               ...              ...               ...                 ...   \n",
       "2373                0                0                 0                   1   \n",
       "2374                0                0                 0                   0   \n",
       "2375                0                0                 0                   0   \n",
       "2376                0                0                 0                   0   \n",
       "2377                0                0                 0                   1   \n",
       "\n",
       "      Brand_name_Jeep  Brand_name_KIA  Brand_name_MG  ...  Brand_name_Maruti  \\\n",
       "0                   0               0              0  ...                  0   \n",
       "1                   0               0              0  ...                  1   \n",
       "2                   0               0              0  ...                  1   \n",
       "3                   0               0              0  ...                  0   \n",
       "4                   0               0              0  ...                  1   \n",
       "...               ...             ...            ...  ...                ...   \n",
       "2373                0               0              0  ...                  0   \n",
       "2374                0               0              0  ...                  0   \n",
       "2375                1               0              0  ...                  0   \n",
       "2376                0               0              0  ...                  1   \n",
       "2377                0               0              0  ...                  0   \n",
       "\n",
       "      Brand_name_Mercedes  Brand_name_Nissan  Brand_name_Renault  \\\n",
       "0                       0                  0                   0   \n",
       "1                       0                  0                   0   \n",
       "2                       0                  0                   0   \n",
       "3                       0                  0                   0   \n",
       "4                       0                  0                   0   \n",
       "...                   ...                ...                 ...   \n",
       "2373                    0                  0                   0   \n",
       "2374                    0                  0                   0   \n",
       "2375                    0                  0                   0   \n",
       "2376                    0                  0                   0   \n",
       "2377                    0                  0                   0   \n",
       "\n",
       "      Brand_name_Skoda  Brand_name_Ssangyong  Brand_name_Tata  \\\n",
       "0                    0                     0                1   \n",
       "1                    0                     0                0   \n",
       "2                    0                     0                0   \n",
       "3                    0                     0                0   \n",
       "4                    0                     0                0   \n",
       "...                ...                   ...              ...   \n",
       "2373                 0                     0                0   \n",
       "2374                 0                     0                0   \n",
       "2375                 0                     0                0   \n",
       "2376                 0                     0                0   \n",
       "2377                 0                     0                0   \n",
       "\n",
       "      Brand_name_Toyota  Brand_name_Volkswagen  Brand_name_Volvo  \n",
       "0                     0                      0                 0  \n",
       "1                     0                      0                 0  \n",
       "2                     0                      0                 0  \n",
       "3                     0                      0                 0  \n",
       "4                     0                      0                 0  \n",
       "...                 ...                    ...               ...  \n",
       "2373                  0                      0                 0  \n",
       "2374                  0                      0                 0  \n",
       "2375                  0                      0                 0  \n",
       "2376                  0                      0                 0  \n",
       "2377                  0                      0                 0  \n",
       "\n",
       "[2378 rows x 21 columns]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_v[['Brand_name_BMW', 'Brand_name_Chevrolet', 'Brand_name_Datsun',\n",
    "       'Brand_name_Fiat', 'Brand_name_Ford', 'Brand_name_Honda',\n",
    "       'Brand_name_Hyundai', 'Brand_name_Jeep', 'Brand_name_KIA',\n",
    "       'Brand_name_MG', 'Brand_name_Mahindra', 'Brand_name_Maruti',\n",
    "       'Brand_name_Mercedes', 'Brand_name_Nissan', 'Brand_name_Renault',\n",
    "       'Brand_name_Skoda', 'Brand_name_Ssangyong', 'Brand_name_Tata',\n",
    "       'Brand_name_Toyota', 'Brand_name_Volkswagen', 'Brand_name_Volvo']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:21.613039Z",
     "start_time": "2021-03-27T07:34:21.604845Z"
    }
   },
   "outputs": [],
   "source": [
    "d = [cat_v,numerical_df]\n",
    "final_df = pd.concat(d,join='outer',axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:21.876972Z",
     "start_time": "2021-03-27T07:34:21.815945Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Years</th>\n",
       "      <th>Brand_name_BMW</th>\n",
       "      <th>Brand_name_Chevrolet</th>\n",
       "      <th>Brand_name_Datsun</th>\n",
       "      <th>Brand_name_Fiat</th>\n",
       "      <th>Brand_name_Ford</th>\n",
       "      <th>Brand_name_Honda</th>\n",
       "      <th>Brand_name_Hyundai</th>\n",
       "      <th>Brand_name_Jeep</th>\n",
       "      <th>Brand_name_KIA</th>\n",
       "      <th>...</th>\n",
       "      <th>Insurance_Type_Comprehensive</th>\n",
       "      <th>Insurance_Type_Expired</th>\n",
       "      <th>Insurance_Type_Insurance Expired</th>\n",
       "      <th>Insurance_Type_Third_party</th>\n",
       "      <th>Insurance_Type_Zero Depreciation</th>\n",
       "      <th>Insurance_Type_Zero_Dep</th>\n",
       "      <th>RTO_Other_State</th>\n",
       "      <th>Transmission_Type_MANUAL</th>\n",
       "      <th>Kilometers</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4.699031</td>\n",
       "      <td>114899.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4.291746</td>\n",
       "      <td>368499.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4.760799</td>\n",
       "      <td>196199.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4.676209</td>\n",
       "      <td>156460.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4.125058</td>\n",
       "      <td>293447.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 41 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Years  Brand_name_BMW  Brand_name_Chevrolet  Brand_name_Datsun  \\\n",
       "0      7               0                     0                  0   \n",
       "1      5               0                     0                  0   \n",
       "2     10               0                     0                  0   \n",
       "3     11               0                     0                  0   \n",
       "4      5               0                     0                  0   \n",
       "\n",
       "   Brand_name_Fiat  Brand_name_Ford  Brand_name_Honda  Brand_name_Hyundai  \\\n",
       "0                0                0                 0                   0   \n",
       "1                0                0                 0                   0   \n",
       "2                0                0                 0                   0   \n",
       "3                0                0                 0                   1   \n",
       "4                0                0                 0                   0   \n",
       "\n",
       "   Brand_name_Jeep  Brand_name_KIA  ...  Insurance_Type_Comprehensive  \\\n",
       "0                0               0  ...                             0   \n",
       "1                0               0  ...                             0   \n",
       "2                0               0  ...                             0   \n",
       "3                0               0  ...                             0   \n",
       "4                0               0  ...                             0   \n",
       "\n",
       "   Insurance_Type_Expired  Insurance_Type_Insurance Expired  \\\n",
       "0                       0                                 0   \n",
       "1                       0                                 0   \n",
       "2                       0                                 0   \n",
       "3                       0                                 0   \n",
       "4                       1                                 0   \n",
       "\n",
       "   Insurance_Type_Third_party  Insurance_Type_Zero Depreciation  \\\n",
       "0                           0                                 0   \n",
       "1                           0                                 0   \n",
       "2                           1                                 0   \n",
       "3                           0                                 0   \n",
       "4                           0                                 0   \n",
       "\n",
       "   Insurance_Type_Zero_Dep  RTO_Other_State  Transmission_Type_MANUAL  \\\n",
       "0                        0                0                         1   \n",
       "1                        1                0                         0   \n",
       "2                        0                0                         1   \n",
       "3                        0                0                         1   \n",
       "4                        0                0                         1   \n",
       "\n",
       "   Kilometers     Price  \n",
       "0    4.699031  114899.0  \n",
       "1    4.291746  368499.0  \n",
       "2    4.760799  196199.0  \n",
       "3    4.676209  156460.0  \n",
       "4    4.125058  293447.0  \n",
       "\n",
       "[5 rows x 41 columns]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:22.071054Z",
     "start_time": "2021-03-27T07:34:22.036071Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Years', 'Brand_name_BMW', 'Brand_name_Chevrolet', 'Brand_name_Datsun',\n",
       "       'Brand_name_Fiat', 'Brand_name_Ford', 'Brand_name_Honda',\n",
       "       'Brand_name_Hyundai', 'Brand_name_Jeep', 'Brand_name_KIA',\n",
       "       'Brand_name_MG', 'Brand_name_Mahindra', 'Brand_name_Maruti',\n",
       "       'Brand_name_Mercedes', 'Brand_name_Nissan', 'Brand_name_Renault',\n",
       "       'Brand_name_Skoda', 'Brand_name_Ssangyong', 'Brand_name_Tata',\n",
       "       'Brand_name_Toyota', 'Brand_name_Volkswagen', 'Brand_name_Volvo',\n",
       "       'Fuel_Type_Petrol', 'Fuel_Type_Petrol + CNG', 'Fuel_Type_Petrol + LPG',\n",
       "       'Owner_Type_First Owner', 'Owner_Type_Fourth Owner',\n",
       "       'Owner_Type_Second Owner', 'Owner_Type_Sixth Owner',\n",
       "       'Owner_Type_Third Owner', 'Insurance_Type_Comp',\n",
       "       'Insurance_Type_Comprehensive', 'Insurance_Type_Expired',\n",
       "       'Insurance_Type_Insurance Expired', 'Insurance_Type_Third_party',\n",
       "       'Insurance_Type_Zero Depreciation', 'Insurance_Type_Zero_Dep',\n",
       "       'RTO_Other_State', 'Transmission_Type_MANUAL', 'Kilometers', 'Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:22.491493Z",
     "start_time": "2021-03-27T07:34:22.483732Z"
    }
   },
   "outputs": [],
   "source": [
    "final_df.columns = [c.replace('+', '') for c in final_df.columns]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:22.709294Z",
     "start_time": "2021-03-27T07:34:22.703160Z"
    }
   },
   "outputs": [],
   "source": [
    "final_df.columns = [c.replace('  ', ' ') for c in final_df.columns]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:23.117530Z",
     "start_time": "2021-03-27T07:34:23.096886Z"
    }
   },
   "outputs": [],
   "source": [
    "final_df.columns = [c.replace(' ', '_') for c in final_df.columns]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:23.274252Z",
     "start_time": "2021-03-27T07:34:23.258318Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Years', 'Brand_name_BMW', 'Brand_name_Chevrolet', 'Brand_name_Datsun',\n",
       "       'Brand_name_Fiat', 'Brand_name_Ford', 'Brand_name_Honda',\n",
       "       'Brand_name_Hyundai', 'Brand_name_Jeep', 'Brand_name_KIA',\n",
       "       'Brand_name_MG', 'Brand_name_Mahindra', 'Brand_name_Maruti',\n",
       "       'Brand_name_Mercedes', 'Brand_name_Nissan', 'Brand_name_Renault',\n",
       "       'Brand_name_Skoda', 'Brand_name_Ssangyong', 'Brand_name_Tata',\n",
       "       'Brand_name_Toyota', 'Brand_name_Volkswagen', 'Brand_name_Volvo',\n",
       "       'Fuel_Type_Petrol', 'Fuel_Type_Petrol_CNG', 'Fuel_Type_Petrol_LPG',\n",
       "       'Owner_Type_First_Owner', 'Owner_Type_Fourth_Owner',\n",
       "       'Owner_Type_Second_Owner', 'Owner_Type_Sixth_Owner',\n",
       "       'Owner_Type_Third_Owner', 'Insurance_Type_Comp',\n",
       "       'Insurance_Type_Comprehensive', 'Insurance_Type_Expired',\n",
       "       'Insurance_Type_Insurance_Expired', 'Insurance_Type_Third_party',\n",
       "       'Insurance_Type_Zero_Depreciation', 'Insurance_Type_Zero_Dep',\n",
       "       'RTO_Other_State', 'Transmission_Type_MANUAL', 'Kilometers', 'Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:23.463858Z",
     "start_time": "2021-03-27T07:34:23.454369Z"
    }
   },
   "outputs": [],
   "source": [
    "# import seaborn as sns\n",
    "# plt.figure(figsize=(10,10))\n",
    "# sns.heatmap(final_df.corr(),cmap='viridis',annot=True, square=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:23.643098Z",
     "start_time": "2021-03-27T07:34:23.626029Z"
    }
   },
   "outputs": [],
   "source": [
    "X = final_df.drop(['Price'],1)\n",
    "y = final_df['Price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:24.291513Z",
     "start_time": "2021-03-27T07:34:24.279327Z"
    }
   },
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:24.526290Z",
     "start_time": "2021-03-27T07:34:24.511956Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'n_estimators': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200], 'max_features': ['auto', 'sqrt'], 'max_depth': [5, 10, 15, 20, 25, 30], 'min_samples_split': [2, 5, 10, 15, 100], 'min_samples_leaf': [1, 2, 5, 10]}\n"
     ]
    }
   ],
   "source": [
    "#Randomized Search CV\n",
    "\n",
    "# Number of trees in random forest\n",
    "n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]\n",
    "\n",
    "# Number of features to consider at every split\n",
    "max_features = ['auto', 'sqrt']\n",
    "\n",
    "# Maximum number of levels in tree\n",
    "max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]\n",
    "# max_depth.append(None)\n",
    "\n",
    "# Minimum number of samples required to split a node\n",
    "min_samples_split = [2, 5, 10, 15, 100]\n",
    "\n",
    "# Minimum number of samples required at each leaf node\n",
    "min_samples_leaf = [1, 2, 5, 10]\n",
    "\n",
    "# Create the random grid\n",
    "random_grid = {'n_estimators': n_estimators,\n",
    "               'max_features': max_features,\n",
    "               'max_depth': max_depth,\n",
    "               'min_samples_split': min_samples_split,\n",
    "               'min_samples_leaf': min_samples_leaf}\n",
    "\n",
    "print(random_grid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:34:24.916523Z",
     "start_time": "2021-03-27T07:34:24.896226Z"
    }
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:35:54.832210Z",
     "start_time": "2021-03-27T07:34:25.102227Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 10 candidates, totalling 50 fits\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   1.6s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   1.5s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   1.4s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   1.4s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   1.8s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.9s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.8s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.8s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.8s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.8s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.8s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.8s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.8s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.8s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.8s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   1.4s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   1.4s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   1.4s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   1.4s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   1.4s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   2.2s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   2.2s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   2.1s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   2.2s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   2.1s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   2.4s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   2.5s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   2.4s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   2.4s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   2.4s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.5s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.4s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.4s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.4s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.4s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.5s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.5s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.5s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.5s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.6s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   1.0s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   2.8s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   2.8s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   3.8s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   2.8s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   2.7s\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "RandomizedSearchCV(cv=5, estimator=RandomForestRegressor(), n_jobs=1,\n",
       "                   param_distributions={'max_depth': [5, 10, 15, 20, 25, 30],\n",
       "                                        'max_features': ['auto', 'sqrt'],\n",
       "                                        'min_samples_leaf': [1, 2, 5, 10],\n",
       "                                        'min_samples_split': [2, 5, 10, 15,\n",
       "                                                              100],\n",
       "                                        'n_estimators': [100, 200, 300, 400,\n",
       "                                                         500, 600, 700, 800,\n",
       "                                                         900, 1000, 1100,\n",
       "                                                         1200]},\n",
       "                   random_state=42, scoring='neg_mean_squared_error',\n",
       "                   verbose=2)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the random grid to search for best hyperparameters\n",
    "# First create the base model to tune\n",
    "rf = RandomForestRegressor()\n",
    "# Random search of parameters, using 3 fold cross validation, \n",
    "# search across 100 different combinations\n",
    "rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 10, cv = 5, verbose=2, random_state=42, n_jobs = 1)\n",
    "rf_random.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T07:40:43.451637Z",
     "start_time": "2021-03-27T07:40:43.350007Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RMSE: 433.6183237381137\n"
     ]
    }
   ],
   "source": [
    "ypred = rf_random.predict(X_test)\n",
    "mse = mean_squared_error(ypred, y_test, squared=False)\n",
    "rmse = np.sqrt(mse)\n",
    "print('RMSE:',rmse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T06:00:17.490581Z",
     "start_time": "2021-03-27T06:00:17.451393Z"
    }
   },
   "outputs": [],
   "source": [
    "# save the model to disk\n",
    "filename = 'finalized_model (1).pkl'\n",
    "pickle.dump(rf_random, open(filename, 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-03-27T06:01:05.764978Z",
     "start_time": "2021-03-27T06:01:05.593235Z"
    },
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[317999.65599206 387839.3886416  318137.99356395 308523.19178837\n",
      " 331827.82509599 307256.90321406 320179.08235907 357887.14442921\n",
      " 343678.46205294 445360.25268882 353077.01271535 340022.18712761\n",
      " 245836.91410789 307462.30123338 355256.61967837 313672.63020597\n",
      " 160183.87292388 304271.06218574 357441.5885498  315820.16373099\n",
      " 356785.27425807 394152.78896008 305529.65731235 325904.31398423\n",
      " 799885.3663649  170388.79893794 310100.81284931 240926.95050325\n",
      " 320583.88950152 369870.77099674 286018.85196886 309096.07890741\n",
      " 328143.23302116 332510.01022513 333792.51411023 334600.45312136\n",
      " 354405.05665614 279578.87922971 301212.30724465 418544.9561375\n",
      " 321274.72392445 466659.08707498 363032.09512886 343417.57968819\n",
      " 430105.56349676 284543.78432772 278475.22939277 328087.31864942\n",
      " 363433.71116054 332055.82260413 261879.19783999 314812.25995639\n",
      " 346698.91703661 330400.59235115 240641.55369522 372988.75926925\n",
      " 306526.47153549 296987.04272358 478649.77766398 423116.11380944\n",
      " 346315.55614476 331163.05388757 302849.69340903 349513.56215654\n",
      " 309835.17022025 351031.54064183 352861.74158313 358519.18970476\n",
      " 343130.68071354 312677.30328955 353290.87525958 322854.63189114\n",
      " 251272.28517291 341342.89615416 343999.09334738 299222.3243993\n",
      " 345129.39311663 310801.78378764 251260.65460864 366993.37647188\n",
      " 347329.13155333 344066.43845589 258044.7322175  480251.40090612\n",
      " 465836.31320365 348412.92195474 340264.78031518 364580.26698129\n",
      " 310492.50682994 325534.7344438  375806.80956794 360405.19485868\n",
      " 359145.61200235 330194.95883778 195465.8497103  337299.25633955\n",
      " 317253.56880572 311070.42926935 341603.03171099 365396.59650985\n",
      " 399767.27261859 411934.05338019 274748.71257631 372375.77717914\n",
      " 331218.14172402 336262.16262278 300450.19775911 391053.69906001\n",
      " 306994.00144782 293705.85837718 350449.29623784 338956.88635666\n",
      " 372759.79986969 332612.58597437 399570.5287245  319639.05328602\n",
      " 314126.22523931 328602.69792063 413776.46013868 400556.94890486\n",
      " 341638.22669539 172643.48123033 343821.51330421 385696.28362396\n",
      " 306438.29245621 296234.86199424 317550.80653437 334678.87704536\n",
      " 315577.49049011 324401.76754295 301500.82650896 338415.65503219\n",
      " 308124.87277223 326757.39133983 390925.79282939 306725.69353598\n",
      " 260092.11299334 342139.91826564 292609.89818109 458757.77452182\n",
      " 293248.72904826 378078.03580988 405848.05354962 310742.59470732\n",
      " 320057.6337669  330967.6926557  346664.09187968 336681.99249101\n",
      " 403293.22672563 314493.6472189  361405.68008382 313988.4533885\n",
      " 289085.87990871 385851.47257262 332906.4589594  311169.58010741\n",
      " 372540.56935319 372599.80854952 297077.59488562 404005.1947598\n",
      " 284312.29308688 289984.10822935 392055.88759211 340567.92648553\n",
      " 312043.38516171 335601.14945107 326028.0059346  365185.36684366\n",
      " 331600.67404587 365126.62370791 274161.67572788 366421.57656934\n",
      " 464356.83170225 374352.89728845 272581.02452878 438900.84335215\n",
      " 330307.76950293 330374.39237426 330159.01150446 311759.26602881\n",
      " 284528.89652363 400817.38818696 337010.4414847  285527.27496268\n",
      " 355612.80146851 336390.43315141 333711.17719063 357925.64676507\n",
      " 524546.11605017 361707.5800972  354633.83707754 376216.55714934\n",
      " 354289.76254565 334904.32279167 293490.78323484 333529.33630211\n",
      " 339068.47525184 370185.68025668 326960.15188155 346293.2276747\n",
      " 341940.13938485 305794.09924656 382487.37132019 396938.88172998\n",
      " 353816.24359133 345239.92614972 343800.01620865 294495.1067599\n",
      " 282111.62974198 416570.51702131 366150.37467078 304319.0670236\n",
      " 268057.139083   367875.53560619 344296.52823704 355111.44743475\n",
      " 308676.11446057 331602.90808442 476330.98263838 318840.48111369\n",
      " 350747.73972261 323606.93991855 263593.46096997 408185.93144938\n",
      " 431323.84366557 332738.17544385 385167.47703259 384173.7022818\n",
      " 252202.36401136 310659.18729439 427545.5391171  355951.76726399\n",
      " 314474.0621355  353433.43989655 366518.76436563 321027.65514658\n",
      " 451825.07095017 407591.7762137  419957.42803172 319944.1736614\n",
      " 534314.63472357 318630.80727821 331325.12061736 296953.79540962\n",
      " 286046.71880642 437024.01678278 322748.69006327 337517.01332606\n",
      " 342371.17003316 332794.23731685 363779.6813675  307374.97886535\n",
      " 362397.94812777 298364.5958584  349501.222705   321140.77232419\n",
      " 320638.68947241 321786.59761892 360162.86492574 359847.25091527\n",
      " 318396.85464726 308525.91445569 300299.98288753 190073.44751191\n",
      " 369509.04480157 405253.52661871 191534.95105106 356609.34352969\n",
      " 378884.80675843 305331.16530042 297457.36578067 335663.26070399\n",
      " 328664.9470138  303948.8558601  312199.25921124 341295.10284487\n",
      " 309199.51070724 335752.39205074 341168.61649477 322299.67152964\n",
      " 270039.44435503 333048.82102623 335199.69844269 320884.65504247\n",
      " 356388.50346834 356431.02799603 374256.01680797 178897.03439031\n",
      " 378464.45400145 325144.17275791 345300.87021966 445761.21934237\n",
      " 441182.32865657 345724.29131528 320365.51838027 367688.45133139\n",
      " 325450.66648322 317516.15991493 315795.89284429 348925.98476494\n",
      " 434737.64984228 398841.10280798 316517.22726725 342929.97830119\n",
      " 334217.30367033 367099.75034279 294346.36089579 331033.24513835\n",
      " 319770.2654868  330094.93554486 177703.74000359 352892.17091034\n",
      " 409643.73042257 356796.05354136 362128.61013211 350743.07264754\n",
      " 330684.14876338 448431.9935588  308162.4843926  352672.83501032\n",
      " 281049.96898107 347162.51542326 335803.60452378 313181.60638747\n",
      " 337777.37269892 368560.55180222 411144.08536961 316694.49058514\n",
      " 297316.46024343 324405.51450927 342767.92254394 298994.50231948\n",
      " 317574.6100311  333692.07091422 161923.33941034 329458.19756058\n",
      " 314996.41076154 333113.68611773 367542.61777269 332607.6117862\n",
      " 338317.55904179 364821.06629717 325188.6426824  384482.10018511\n",
      " 333133.57388834 410089.31452667 339574.3687783  418001.79664138\n",
      " 381688.79457278 345527.445081   359810.89065549 294567.46515883\n",
      " 347800.75520163 315461.19528912 340202.1671642  436330.1900663\n",
      " 317846.3002489  377196.85504077 345896.33341859 327597.2865807\n",
      " 400100.80805395 347906.7611014  362475.00330124 333877.5241595\n",
      " 309309.01332624 354675.65244263 320458.00193148 296951.17873089\n",
      " 391339.97944846 375038.15357284 328334.69268682 321644.9841223\n",
      " 325040.48885459 389577.04831296 305275.64185119 380136.5244884\n",
      " 327754.327593   321328.65521776 373718.46778047 348649.07535844\n",
      " 279723.24525113 348904.35372745 318208.54370001 349175.63719644\n",
      " 277202.78928256 338232.22851673 401197.64029834 351678.89823491\n",
      " 268354.46453968 257590.50190244 318427.36934801 166148.48433715\n",
      " 365341.17127798 317312.90604244 361297.10101556 312085.52597467\n",
      " 353344.16992128 341384.34740883 352439.8607726  361866.84234247\n",
      " 338278.77173567 348832.65997772 398275.08852943 278002.13966696\n",
      " 361183.23550257 320678.64994796 299271.52237771 441693.22783034\n",
      " 322468.67856672 387972.90043886 265110.53384509 381629.76396769\n",
      " 396093.63187952 396692.63691151 377472.89785021 412480.43380254\n",
      " 557072.79993769 337699.78326013 340397.12972617 307391.94273295\n",
      " 290855.11267532 299467.50168246 416814.85077891 346050.23086443\n",
      " 327869.01922165 323864.1953455  293041.56076418 340218.32428599\n",
      " 384381.40228199 382583.50737791 333657.26948979 311496.00557254\n",
      " 355190.35314253 271403.78754257 287444.5039845  383927.98759941\n",
      " 401344.0980087  296508.19757849 311672.56276458 319464.46864831\n",
      " 354730.98034637 341001.97270702 353180.46770447 286971.59404441\n",
      " 365038.88859803 323189.20147707 341333.65797784 410826.63321344\n",
      " 321515.4398827  471056.67888852 350528.82179846 333041.37597228\n",
      " 284970.30737478 414534.69078147 324986.55704623 316251.92331504\n",
      " 346880.77406885 366380.03823726 353624.62987341 307019.74704125\n",
      " 401380.81185904 312341.20171362 266125.24776462 334071.49855272\n",
      " 379672.26716918 284519.71246631 312827.05199301 310874.7355183\n",
      " 306234.74050218 446162.48355074 358025.35495973 309058.16900904\n",
      " 306093.26689752 296760.99516019 320345.42570032 317171.05270057\n",
      " 368769.56629039 399380.32405067 314053.93715815 300507.2541097\n",
      " 409586.54303568 365946.25135089 361900.99088379 296835.03774017\n",
      " 288826.99938174 466728.41564335 324930.21315808 329818.55621195\n",
      " 379608.94089818 308795.64221394 364224.83479093 311102.17846813\n",
      " 356359.60169578 317473.82875059 346903.65842366 291444.59453708\n",
      " 414466.04994542 308420.0797285  337073.44864071 341360.14237594\n",
      " 288846.33827103 369901.40278673 366084.41262524 316168.87576253\n",
      " 325992.80342095 348731.32966009 356337.77875771 321970.44554428\n",
      " 254193.12812352 181387.27738142 320433.26938913 424592.20581235\n",
      " 288804.4538892  344922.81725669 437444.44493158 337307.74323837\n",
      " 336651.2561411  325469.87318921 353433.43989655 344225.78222354\n",
      " 353846.83709577 340870.88829119 312012.80630062 368803.92924196\n",
      " 333668.9149864  409190.44768582 163278.73524779 372178.57635196\n",
      " 372397.37070956 302398.25910469 348266.85818407 338508.24782353\n",
      " 364132.36899877 309454.96221512 311487.77616217 284365.26077229\n",
      " 334007.29657808 343958.77728153 316672.41214021 316291.80738237\n",
      " 320573.2298757  331944.73050626 332059.29244169 394596.0936907\n",
      " 284765.62228237 360001.26470985 406556.82329741 351854.57440531\n",
      " 333491.14547037 340334.34513351 314585.2403066  296221.89529408\n",
      " 315099.56149721 371864.98206903 333959.97882863 344570.29969827\n",
      " 311425.9241927  409097.95384543 347638.47711827 343587.28974266\n",
      " 395494.53992437 399209.81173797 421658.4385647  382089.54489999\n",
      " 388882.83280933 470335.30984013 332367.22379783 163712.07194515\n",
      " 327117.641746   320208.82085135 381887.9969501  351455.12980303\n",
      " 360442.07465119 264495.91930956 371359.15584963 323361.7362813\n",
      " 429315.05759833 384116.65745982 329519.97380219 313360.689285\n",
      " 356924.70459801 378073.84451149 320037.86663139 357039.09823424\n",
      " 311431.90230465 396538.11315454 327392.99877011 170635.44583559\n",
      " 345593.02163866 355978.81256396 307983.21861513 326785.25411658\n",
      " 457838.54443973 402222.3849958  380035.13381033 363215.37637796\n",
      " 327572.08027869 263958.94539122 287926.52858334 338242.16480474\n",
      " 342834.2958472  332162.12407323 355737.68211277 341285.94585309\n",
      " 443918.05100782 357037.90800547 329342.26339258 374070.90864982\n",
      " 347491.66302912 348901.87732689 395568.14343523 324915.41493315\n",
      " 331597.41225219 333740.92955948 313613.41638259 465586.93831506\n",
      " 368538.87969898 321344.349507   359903.39278689 366794.58311757\n",
      " 293804.25706916 374806.7511615  372485.80639767 335207.53152411\n",
      " 350446.12731326 354677.02527259 337999.80014936 274122.36499826\n",
      " 323436.8340423  400916.98500702 354535.09727933 357146.33474412\n",
      " 368314.96221285 342095.11524643 288147.75784358 346510.82633162\n",
      " 330258.37888953 349513.54255077 431898.19442131 347484.60303468\n",
      " 413625.84019893 418410.18063172 329848.85100452 305024.49429257\n",
      " 340288.45156532 309727.95841702 358106.78926298 344091.01308092\n",
      " 307633.37206364 339574.14844517 326122.13220922 326039.98976535\n",
      " 309552.09642865 419017.64259195 337557.4809067  406260.2615717\n",
      " 419248.52245771 326584.14975977 349798.32083884 304562.25869505\n",
      " 338657.26216696 311823.70428308 328394.49166444 323401.01850006\n",
      " 296692.16289626 310307.01101613 357114.54803389 443852.96950365\n",
      " 312108.92467773 392091.12035591 321390.07918814 299077.4422948\n",
      " 172344.9356794  312013.14590278 344413.83891927 343768.20858201\n",
      " 302947.64604169 350702.17583936 325755.2014283  403374.74708033\n",
      " 390278.8503048  353478.39483156 355600.43629597 450781.06878792\n",
      " 319296.96031039 259174.06836237 316444.21581077 420021.67048188\n",
      " 345974.31389497 392845.69026453 307960.4121243  300306.27815776\n",
      " 373951.78079385 336502.43656095 360982.98882264 355902.5194486\n",
      " 309907.02596981 338662.22507308 374372.27939762 365634.51032659\n",
      " 386803.5575905  301115.26093456 356403.53029267 351099.6831155\n",
      " 400647.17777065 323619.12326533 421451.43619968 351869.54979887\n",
      " 318020.5931224  197657.55424058 216770.135961   298713.69600847\n",
      " 339860.20237612 350677.50980144]\n"
     ]
    }
   ],
   "source": [
    "# load the model from disk\n",
    "loaded_model = pickle.load(open(filename, 'rb'))\n",
    "result = loaded_model.predict(X_test)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
