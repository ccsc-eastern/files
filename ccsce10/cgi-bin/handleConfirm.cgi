#!/usr/local/bin/perl -w

use CGI ":standard";
use DBI;

#>>> get data from the form
my ($email) = (param("Email"));
my ($prefix) = (param("Prefix"));
my ($firstname) = (param("FirstName"));
my ($middlename) = (param("MiddleName"));
my ($lastname) = (param("LastName"));
my ($suffix) = (param("Suffix"));
my ($badgename) = (param("BadgeName"));
my ($company) = (param("Company"));
my ($address1) = (param("Address1"));
my ($address2) = (param("Address2"));
my ($city) = (param("City"));
my ($state) = (param("SRP"));
my ($zip) = (param("Zip"));
my ($country) = (param("Country"));
my ($phone) = (param("Phone"));
my ($registration_type) = (param("Registration"));
my ($extra_banquet_ticket) = (param("Banquet"));
my ($extra_lunch_ticket) = (param("Lunch"));
my ($extra_proceedings) = (param("Proceedings"));
my ($fridayWShop) = (param("FridayWShop"));
my ($saturdayWShop) = (param("SaturdayWShop"));
my ($totalregcost) = (param("Cost"));


my $time = time();

#>>> access the database
my $dbh = DBI->connect("DBI:mysql:xxxxxx","ccsce","xxxxxxxxx");

my $testQ = "insert into registrations 
(
email,
prefix,
firstname,
middlename,
lastname,
suffix,
badgename,
company,
address1,
address2,
city,
state,
zip,
country,
phone,
registration_type,
extra_banquet_ticket,
extra_lunch_ticket,
extra_proceedings,
fridayWShop,
saturdayWShop,
totalregcost,
timestamp
)
values
(
'$email',
'$prefix',
'$firstname',
'$middlename',
'$lastname',
'$suffix',
'$badgename',
'$company',
'$address1',
'$address2',
'$city',
'$state',
'$zip',
'$country',
'$phone',
'$registration_type',
'$extra_banquet_ticket',
'$extra_lunch_ticket',
'$extra_proceedings',
'$fridayWShop',
'$saturdayWShop',
'$totalregcost',
'$time'
)";

my $teststh = $dbh->prepare($testQ);
$teststh->execute;

#>>>or
#>>>die "Error -- unable to open database, please contact conference chair\n";


#>>> Create web page to return to user 

# development link
# $link = "http://inbdev.villanova.edu:9050/pls/bannertest/bvskcpmt.P_CreditCardPayment?no_items_in=$totalregcost&pay_code=CCSCEC&data_2=$time";

# production link
$link = "https://novasis.villanova.edu/pls/bannerprd/bvskcpmt.P_CreditCardPayment?no_items_in=$totalregcost&pay_code=CCSCEC&data_2=$time";

# print header;
# print start_html("hi");
# print $link;
# print end_html;

print "Location: ",$link,"\n\n";


