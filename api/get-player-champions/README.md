
### Get Player Champions

**Request**: <i>/**GetPlayerChampions**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetPlayerChampions”</b> method</td>
		<td>“a3360d5cab2740797dc297af77af46f5”</td>
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
	<tr>
		<td>player_id</td>
		<td><a href="./../api-parameter-details.md#player-id" title="Player Id">player id</a> of the <a href="./../api-parameter-details.md#player" title="Player">Player</a> you want to get info on</td>
		<td>“5691962”</td>
	</tr>
</table>

**Response**: JSON
``` json
[
 {
  "Champion":"Androxus",
  "ChampionId":2205,
  "OwnershipType":"Purchased",
  "PlayerId":5691962,
  "XP":61252810,
  "ret_msg":null
 }
]
```
