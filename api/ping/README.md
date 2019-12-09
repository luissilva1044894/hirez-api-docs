
## Ping

<!--A quick way of validating access (establish connectivity) to the API, which indicates whether the request was successful.-->
A quick way of validating availabiltiy of the API, which indicates whether the request was successful.

Pinging the API is used to ensure that you have access to the API as you do not need to [authenticate](api-parameter-details.md#session-authentication) your [API Key](api-parameter-details.md#api-key).

**Request**: <i>/**Ping**[response_type]</i> `GET` 
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
	</tr>
</table>

**Response**: JSON

```json
"PaladinsAPI (ver 0.0.41.18898) [PATCH - 2.11] - Ping successful. Server Date:11/28/2019 3:09:16 PM"
```

**Response**: XML
```xml
<string>
 SmiteAPI (ver 3.24.0.26013) [PATCH - 6.12] - Ping successful. Server Date:11/28/2019 3:09:16 PM
</string>
```
