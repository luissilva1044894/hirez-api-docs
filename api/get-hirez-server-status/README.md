
## Get Hi-Rez Server Status
>DATA IS CACHED ONCE A MINUTE.

Returns UP/DOWN status for the primary game/platform environments.

**Request**: <i>/**GetHiRezServerStatus**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetHiRezServerStatus”</b> method</td>
		<td>“14ddf0d9fa2ce9e3d30ddb7647c82a73”</td>
	</tr>
	<tr>
		<td>session_id</td>
		<td>A valid <a href="./../#sessions">Session</a></td>
		<td>1465AFCA32DBDB800CEF8C72F296C52C</td>
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
 	 "entry_datetime": "2019-11-28 15:26:09.545",
 	 "environment": "live",
 	 "limited_access": false,
 	 "platform": "pc",
 	 "ret_msg": null,
 	 "status": "UP",
 	 "version": "2.11.3416.15"
 }
]
```
