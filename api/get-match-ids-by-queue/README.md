
## Get Match IDs By Queue

Lists all <a href="./../api-parameter-details.md#match-id" title="Match Id">Match IDs</a> values for a particular <a href="./../api-parameter-details.md#game-mode" title="Game Mode">Game Mode</a> for a particular timeframe. Useful for API developers interested in constructing data by <a href="./../api-parameter-details.md#game-mode" title="Game Mode">Game Mode</a>.

**Request**:
<i>/**GetMatchIDsByQueue**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{queue_id}/{date}/{hour}</i> `GET`

<table>
	<tr>
		<th>URI Parameter</th>
		<th>Description</th>
		<th>Example</th>
	</tr>
	<tr>
		<td>response_type</td>
		<td>A valid <a href="./../api-parameter-details.md#response-type" title="Response Type">Response Type</a></td>
		<td>“json”</td>
	</tr>
	<tr>
		<td>dev_id</td>
		<td>The dev_id from your <a href="./../api-parameter-details.md#credentials" title="Credentials">Credentials</a></td>
		<td>“1004”</td>
	</tr>
	<tr>
		<td>signature</td>
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetMatchIDsByQueue”</b> method</td>
		<td>“1d698555193f812f580b7f6dd9a0d520”</td>
	</tr>
	<tr>
		<td>timestamp</td>
		<td>A valid <a href="./../api-parameter-details.md#timestamp" title="Timestamp">Timestamp</a></td>
		<td>“20191128030916”</td>
	</tr>
	<tr>
		<td>queue_id</td>
		<td>A valid <a href="./../api-parameter-details.md#queue-id" title="Queue ID">Game Mode ID</a></td>
		<td>476</td>
	</tr>
	<tr>
		<td>date</td>
		<td>A valid <a href="./../api-parameter-details.md#date" title="Data">Date</a></td>
		<td></td>
	</tr>
	<tr>
		<td>hour</td>
		<td>To limit the data returned, a <a href="./../api-parameter-details.md#hour" title="Hour">Hour</a> parameter was added.<br/>An hour parameter of -1 represents the entire day, but be warned that this may be more data than we can return for certain queues.</td>
		<td></td>
	</tr>
</table>

**Response**: JSON
```json
[
 {
 	"Active_Flag": "n",
 	"Match": "908700844",
 	"ret_msg": null
 }
]
```

**Response Details**:
<table>
	<tr>
		<th>Parameter</th>
		<th>Description</th>
	<tr>
		<td>Active_Flag</td>
		<td>A returned “active_flag” means that there is no match information/stats for the corresponding match. Usually due to a match being in-progress, though there could be other reasons.</td>
	</tr>
	<tr>
		<td>Match</td>
		<td><a href="./../api-parameter-details.md#match-id" title="Match Id">Match ID</a></td>
	</tr>
	<tr>
		<td>ret_msg</td>
		<td><a href="./../README.md#ret-msg" title="ret_msg">ret_msg</a></td>
	</tr>
</table>



