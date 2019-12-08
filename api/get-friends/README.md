
## Get Friends

Returns all friends of a given player.

**Request**: <i>/**GetFriends**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetFriends”</b> method</td>
		<td>1105efae92f8db89460895d976292940</td>
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
	<tr>
		<td>player_id</td>
		<td>A valid <a href="./../api-parameter-details.md#player-id" title="Player ID">Player ID</a></td>
		<td>987654321</td>
	</tr>
</table>
<br/><br/>

**Response**: JSON
```json
[
 {
  "account_id":"11890573",
  "avatar_url":"http://cds.q6u4m8x5.hwcdn.net/web/smite-app//wp-content/uploads/2016/10/Allied_Strong.png",
  "name":"mogens123",
  "player_id":"5689086",
  "ret_msg":null
 }
]
```
