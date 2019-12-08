
## Create Session
>A required step to Authenticate the developer Id/signature for further API use.

Create a new authentication Session ID for requests that require authentication.

The [``Session``](./../README.md#session-authentication) is contained in an element called “<i>``session_id``</i>”. This parameter is needed to call the other methods.

With exception of [``CreateSession``](#create-session) and [``Ping``](./../ping#ping), all endpoints require authentication, so there is no concept of unauthenticated calls and rate limits.

**Request**: <i>/**CreateSession**[response_type]/{dev_id}/{signature}/{timestamp}</i> `GET` 
<table>
	<tr>
		<th>URI Parameter</th>
		<th>Description</th>
		<th>Example</th>
	</tr>
	<tr>
		<td>response_type</td>
		<td>A valid <a href="./../api-parameter-details.md#response_type" title="Response Type">Response Type</a></td>
		<td>json</td>
	</tr>
	<tr>
		<td>dev_id</td>
		<td>The dev_id from your <a href="./../api-parameter-details.md#credentials" title="Credentials">Credentials</a></td>
		<td>1004</td>
	</tr>
	<tr>
		<td>signature</td>
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“CreateSession”</b> method</td>
		<td>de9a8114c56e02abd057a0f2d9671b7d</td>
	</tr>
	<tr>
		<td>timestamp</td>
		<td>The current UTC <a href="./../api-parameter-details.md#timestamp" title="Timestamp">Timestamp</a></td>
		<td>20180628012612</td>
	</tr>
</table>

**Response**: JSON
```json
{
 "ret_msg":"Approved",
 "session_id":"4D3064CF27D0473CA4CF142330E97FB5",
 "timestamp":"2/28/2019 3:12:38 PM"
}
```

**Response**: XML
```XML
<Session xmlns="http://schemas.datacontract.org/2004/07/PaladinsApi" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
 <ret_msg>Approved</ret_msg>
 <session_id>4D3064CF27D0473CA4CF142330E97FB5</session_id>
 <timestamp>2/28/2019 3:12:38 PM</timestamp>
</Session>
```
