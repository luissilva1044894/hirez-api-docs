
### Get Bounty Items

**Request**: <i>/**GetGodAltAbilities**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>GetGodAltAbilities</b> method</td>
		<td>“956e475c5a88d2a069c061040816a400”</td>
	</tr>
	<tr>
		<td>session_id</td>
		<td>A valid <a href="./../#sessions">Session</a></td>
		<td>“a4205d5ac1946aa053c2949a841e8397”</td>
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
  	"alt_name":"Loki V2A A02 Sub Device",
  	"alt_position":"2",
  	"god":"Loki",
  	"god_id":1797,
  	"item_id":18614,
  	"ret_msg":null
 }
]
```
