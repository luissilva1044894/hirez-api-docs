
### Get Data Used

Returns API Developer daily usage limits and the current status against those limits.

**Request**: <i>/**GetDataUsed**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}</i> `GET`

<table>
	<tr>
		<th>URI Parameter</th>
		<th>Description</th>
		<th>Example</th>
	</tr>
	<tr>
		<td>response_type</td>
		<td>A valid <a href="./../api-parameter-details.md#response_type" title="Response Type">Response Type</a></td>
		<td>“json”</td>
	</tr>
	<tr>
		<td>dev_id</td>
		<td>The dev_id from your <a href="./../#credentials" title="Credentials">Credentials</a></td>
		<td>“1004”</td>
	</tr>
	<tr>
		<td>signature</td>
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetDataUsed”</b> method</td>
		<td>“dc489392ffe47a068234aba56ee74e0f”</td>
	</tr>
	<tr>
		<td>session_id</td>
		<td>A valid <a href="./../#sessions">Session</a></td>
		<td>“1465AFCA32DBDB800CEF8C72F296C52C”</td>
	</tr>
	<tr>
		<td>timestamp</td>
		<td>A valid <a href="./../api-parameter-details.md#timestamp" title="Timestamp">Timestamp</a></td>
		<td>“20191128030916”</td>
	</tr>
</table>

**Response**: JSON
``` json
[
 {
  "Active_Sessions": 8,
  "Concurrent_Sessions": 50,
  "Request_Limit_Daily": 7500,
  "Session_Cap": 500,
  "Session_Time_Limit": 15,
  "Total_Requests_Today": 19,
  "Total_Sessions_Today": 14,
  "ret_msg": null
 }
]
```
