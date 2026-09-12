from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Employee Salary Tracker</title>

<style>
body{
    font-family:Arial;
    background:#f4f6f9;
    text-align:center;
}

h1{
    color:#005bea;
}

table{
    margin:auto;
    border-collapse:collapse;
    width:80%;
    background:white;
}

th{
    background:#005bea;
    color:white;
}

th,td{
    padding:12px;
    border:1px solid #ddd;
}
</style>

</head>
<body>

<h1>💰 Employee Salary Tracker</h1>
<h3>Version 1.0</h3>

<table>
<tr>
<th>Employee ID</th>
<th>Name</th>
<th>Department</th>
<th>Salary</th>
</tr>

<tr>
<td>EMP001</td>
<td>Sampath</td>
<td>DevOps</td>
<td>₹85,000</td>
</tr>

<tr>
<td>EMP002</td>
<td>Ram</td>
<td>Windows Admin</td>
<td>₹65,000</td>
</tr>

<tr>
<td>EMP003</td>
<td>Jay</td>
<td>Cloud Engineer</td>
<td>₹95,000</td>
</tr>

<tr>
<td>EMP004</td>
<td>Ayyapa</td>
<td>DevOps Engineer</td>
<td>₹90,000</td>
</tr>

<tr>
<td>EMP005</td>
<td>Siva</td>
<td>Linux Administrator</td>
<td>₹75,000</td>
</tr>

</table>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
