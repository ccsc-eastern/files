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
my ($srp) = (param("SRP"));
my ($zip) = (param("Zip"));
my ($country) = (param("Country"));
my ($phone) = (param("Phone"));
my ($registration) = (param("Registration"));
my ($banquet) = (param("Banquet"));
my ($lunch) = (param("Lunch"));
my ($proceedings) = (param("Proceedings"));
my ($fridayWShop) = (param("fridayWShop"));
my ($saturdayWShop) = (param("saturdayWShop"));

#>>> Create web page to return to user 
print header;
print start_html("Reg Form Received");
print "<h3>Please confirm your information before proceeding to the payment page.</h3>";

print "Email: ",$email,"<br /><br />";
print "Name: ",$prefix," ",$firstname," ", $middlename," ", $lastname," ",$suffix,"<br /><br />";
print "Name on Badge: ",$badgename,"<br /><br />";
print "Company: ",$company,"<br /><br />";
print "Address:<br />";
print "&nbsp;&nbsp;&nbsp;",$address1,"<br />";
print "&nbsp;&nbsp;&nbsp;",$address2,"<br />";
print "&nbsp;&nbsp;&nbsp;",$city,", ",$srp,"&nbsp;&nbsp;&nbsp;",$zip,"<br />";
print "&nbsp;&nbsp;&nbsp;",$country,"<br /><br />";
print "Phone: ",$phone,"<br /><br />";

print "Costs: <br />";

print "<table border=\"1\">
<tr><td><b>Category</b></td><td><b>Your Choice</b></td><td><b>Cost</b></td></tr><tr><td>";

$cost = 0;

if ($registration eq "EarlyStandard")
{
  print "Registration Type</td><td> Early, Standard </td><td> \$135";
  $cost = $cost + 135;
}
elsif ($registration eq "EarlyStudent")
{
  print "<Type</td><td> Early, Student </td><td> \$35<br />";
  $cost = $cost + 35;
}
elsif ($registration eq "EarlyTeacher")
{
  print "Type</td><td> Early, Teacher </td><td> \$50<br />";
  $cost = $cost + 50;
}
elsif ($registration eq "LateStandard")
{
  print "Type</td><td> Late, Standard </td><td> \$155<br />";
  $cost = $cost + 155;
}
elsif ($registration eq "LateStudent")
{
  print "Type</td><td> Late, Student </td><td>  \$45<br />";
  $cost = $cost + 45;
}
elsif ($registration eq "LateTeacher")
{
  print "Type</td><td> Late, Teacher </td><td> \$60<br />";
  $cost = $cost + 60;
}
elsif ($registration eq "Vendor")
{
  print "Type</td><td> Vendor </td><td> \$150<br />";
  $cost = $cost + 150;
}

print "</td></tr><tr><td>";

$banqcost = $banquet * 50;
print "Additional Banquet Tickets:</td><td> ",$banquet,"</td><td> \$",$banqcost,"</td></tr><tr><td>";
$cost = $cost + $banqcost;

$lunchcost = $lunch * 25;
print "Additional Lunch Tickets:</td><td> ",$lunch,"</td><td> \$",$lunchcost,"</td></tr><tr><td>";
$cost = $cost + $lunchcost;

$proccost = $proceedings * 25;
print "Additional Proceedings Tickets:</td><td> ",$proceedings,"</td><td> \$",$proccost,"</td></tr>";
$cost = $cost + $proccost;

$wshopcost = 0;
print "<tr><td>Friday Workshop</td><td>";
if ($fridayWShop == 0)
{
  print "None</td><td> \$0";
}
elsif ($fridayWShop == 1)
{
  $wshopcost = $wshopcost + 6;
  print "1: CS Unplugged</td><td> \$6";
}
elsif ($fridayWShop == 2)
{
  $wshopcost = $wshopcost + 6;
  print "2: Puzzle-Based</td><td> \$6";
}
elsif ($fridayWShop == 6)
{
  $wshopcost = $wshopcost + 6;
  print "6: Female Friendly RPRCC</td><td> \$6";
}
print "</td></tr>";

print "<tr><td>Saturday Workshop</td><td>";
if ($saturdayWShop == 0)
{
  print "None</td><td> \$0";
}
elsif ($saturdayWShop == 3)
{
  $wshopcost = $wshopcost + 6;
  print "3: Cooperative Learning</td><td> \$6";
}
elsif ($saturdayWShop == 4)
{
  $wshopcost = $wshopcost + 6;
  print "4: Animated Database</td><td> \$6";
}
elsif ($saturdayWShop == 5)
{
  $wshopcost = $wshopcost + 6;
  print "5: Fast Forward</td><td> \$6";
}

$cost = $cost + $wshopcost;

print "</td></tr></table>";

print "<br />Total Cost: \$", $cost, "<br /><br />";

print "If the above information is not all correct, please use the back button<br />";
print "on your browser to return to the Registration Form, then correct the<br />";
print "information and resubmit. <br /><br />";
print "If the above information is correct, including the Total Cost, then please <br />";
print "continue to the secure Payment Page where you will be asked for your <br />credit card
information, by pressing the following button:<br /><br />";

print "<form action = \"/cgi-bin/ccsce09/handleConfirm.cgi\">";
print "<INPUT TYPE=hidden NAME=Email VALUE=\"$email\">";
print "<INPUT TYPE=hidden NAME=Prefix VALUE=\"$prefix\">";
print "<INPUT TYPE=hidden NAME=FirstName VALUE=\"$firstname\">";
print "<INPUT TYPE=hidden NAME=MiddleName VALUE=\"$middlename\">";
print "<INPUT TYPE=hidden NAME=LastName VALUE=\"$lastname\">";
print "<INPUT TYPE=hidden NAME=Suffix VALUE=\"$suffix\">";
print "<INPUT TYPE=hidden NAME=BadgeName VALUE=\"$badgename\">";
print "<INPUT TYPE=hidden NAME=Company VALUE=\"$company\">";
print "<INPUT TYPE=hidden NAME=Address1 VALUE=\"$address1\">";
print "<INPUT TYPE=hidden NAME=Address2 VALUE=\"$address2\">";
print "<INPUT TYPE=hidden NAME=City VALUE=\"$city\">";
print "<INPUT TYPE=hidden NAME=SRP VALUE=\"$srp\">";
print "<INPUT TYPE=hidden NAME=Zip VALUE=\"$zip\">";
print "<INPUT TYPE=hidden NAME=Country VALUE=\"$country\">";
print "<INPUT TYPE=hidden NAME=Phone VALUE=\"$phone\">";
print "<INPUT TYPE=hidden NAME=Registration VALUE=\"$registration\">";
print "<INPUT TYPE=hidden NAME=Banquet VALUE=\"$banquet\">";
print "<INPUT TYPE=hidden NAME=Lunch VALUE=\"$lunch\">";
print "<INPUT TYPE=hidden NAME=Proceedings VALUE=\"$proceedings\">";
print "<INPUT TYPE=hidden NAME=FridayWShop VALUE=\"$fridayWShop\">";
print "<INPUT TYPE=hidden NAME=SaturdayWShop VALUE=\"$saturdayWShop\">";
print "<INPUT TYPE=hidden NAME=Cost VALUE=\"$cost\">";
print "<input type=\"submit\" value=\"Continue to Secure Payment Page\" />";

print "</form>";

print end_html;

