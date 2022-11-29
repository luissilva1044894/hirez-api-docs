
### Get Player Match History

**Request**: <i>/**GetPlayerMatchHistory**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>GetPlayerMatchHistory</b> method</td>
		<td>“bbe63c46bafa256284a066adf49913fb”</td>
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

### Get Player Match History After Datetime

**Request**: <i>/**GetPlayerMatchHistoryAfterDatetime**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{start_datetime}/{player_id}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>GetPlayerMatchHistoryAfterDatetime</b> method</td>
		<td>“beced04d97e4ae9163b6e405eea34fd7”</td>
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
		<td>start_datetime</td>
		<td>Datetime in the following format <b>yyyyMMddHHmmss</b></td>
		<td>“20191128030916”</td>
	</tr>
	<tr>
		<td>player_id</td>
		<td><a href="./../api-parameter-details.md#player-id" title="Player Id">player id</a> of the <a href="./../api-parameter-details.md#player" title="Player">Player</a> you want to get info on</td>
		<td>“10443859”</td>
	</tr>
</table>

**Response**: JSON
``` json
{
 "id":10443859,
 "matches":[
   {
    "assists":0,
    "class_id":2494,
    "class_name":"Mage",
    "creeps":5,
    "damage":24723,
    "damage_done_in_hand":0,
    "damage_mitigated":0,
    "damage_taken":8698,
    "deaths":3,
    "gold":0,
    "healing_bot":0,
    "healing_player":782.999939,
    "healing_player_self":3980,
    "killing_spree_max":0,
    "kills":5,
    "map_game":"LIVE Royale Map",
    "match_datetime":"2019-12-01T14:27:27",
    "match_duration_secs":1143,
    "match_id":29723475,
    "match_queue_id":476,
    "match_queue_name":"Squad",
    "placement":2,
    "player_id":0,
    "region":"NA",
    "team_id":1767552,
    "time_in_match_minutes":20,
    "time_in_match_secs":1248,
    "wards_mines_placed":0
   }
 ],
 "name":"SeriousMarineTTV",
 "ret_msg":null
}
```
