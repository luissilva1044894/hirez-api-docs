
## Get Talents

Returns all Talents.

**Request**: <i>/**GetTalents**[response_type]/{dev_id}/{signature}/{session_id}/{timestamp}/{language_code}</i> `GET`

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
		<td>The generated <a href="./../api-parameter-details.md#signature" title="Signature">Signature</a> of <b>“GetTalents”</b> method</td>
		<td>0bfa7e5d058b6f824bc1a1553897e13b</td>
	</tr>
	<tr>
		<td>session_id</td>
		<td>A valid <a href="https://github.com/apugh/realm-api-proposal/wiki/Getting-Started#sessions">Session</a></td>
		<td>1465AFCA32DBDB800CEF8C72F296C52C</td>
	</tr>
	<tr>
		<td>timestamp</td>
		<td>The current UTC <a href="./../api-parameter-details.md#timestamp" title="Timestamp">Timestamp</a></td>
		<td>20180628012612</td>
	</tr>
	<tr>
		<td>language_code</td>
		<td>The Language Code that you want results returned in</td>
		<td>1</td>
	</tr>
</table>
<br/><br/>

**Response**: JSON
```json
[
 {
  "category_name":"Talent Vendor Assassin",
  "item_id":23770,
  "loot_table_item_id":49323,
  "ret_msg":null,
  "talent_description":"Forge abilities for 20 less shards.",
  "talent_name":"Ability Efficiency"
 }
]
```

<!--
20191128030916
11/28/2019 3:09:16 PM
-->
