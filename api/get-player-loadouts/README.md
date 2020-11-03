
### Get Player Loadouts

**Request**: <i>/**GetPlayerLoadouts**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id}/{language_code}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetPlayerLoadouts”</b> method</td>
		<td>“b4c9f7fb672b83203e626ec691fca3e9”</td>
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
	<tr>
		<td>language_code</td>
		<td>A valid <a href="./../api-parameter-details.md#language-globe_with_meridians" title="Language Code">Language Code</a></td>
		<td>“1”</td>
	</tr>
</table>
