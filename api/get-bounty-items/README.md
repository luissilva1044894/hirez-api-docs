
### Get Bounty Items

**Request**: <i>/**GetBountyItems**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetBountyItems”</b> method</td>
		<td>“dc489392ffe47a068234aba56ee74e0f”</td>
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
    "active":"y",
    "bounty_item_id1":65950,
    "bounty_item_id2":14144,
    "bounty_item_name":"Winter",
    "final_price":"hidden",
    "initial_price":"hidden",
    "ret_msg":null,
    "sale_end_datetime":"11/3/2020 12:00:00 PM",
    "sale_type":"Decreasing"
  }
]
```
