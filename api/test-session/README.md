
## Test Session

A means of validating that a session is established.

**Request**: <i>/**TestSession**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“TestSession”</b> method</td>
		<td>c345ed71f9b01d104ea34512c06e36ec</td>
	</tr>
	<tr>
		<td>session_id</td>
		<td>A valid <a href="https://github.com/apugh/realm-api-proposal/wiki/Getting-Started#sessions">Session</a></td>
		<td>1465AFCA32DBDB800CEF8C72F296C52C</td>
	</tr>
	<tr>
		<td>timestamp</td>
		<td>The current UTC <a href="./../api-parameter-details.md#timestamp" title="Timestamp">Timestamp</a></td>
		<td>20191128030916</td>
	</tr>
</table>
<br/><br/>

**Response**: Text Plain
```
This was a successful test with the following parameters added: developer: 1004 time:11/28/2019 3:09:16 PM signature: c345ed71f9b01d104ea34512c06e36ec session: 1465AFCA32DBDB800CEF8C72F296C52C
```
