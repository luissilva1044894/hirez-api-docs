
# API Reference

The [Hi-Rez Studios][hi_rez_studios] API returns JSON (or XML) data with players' information including matches, friends, and stats.

## Comercial usage

*If you are interested in creating an App that is paid and/or contains monetization features, please contact us at monetization_requests@hirezstudios.com to discuss a potential business relationship. All for-profit Apps must be pre-approved in writing by Hi-Rez (such approval to be granted or withheld in Hi-Rez's sole discretion). To the extent any for-profit Apps are approved in writing by Hi-Rez (in its sole discretion), you will be solely responsible for any and all taxes due in connection with the distribution of such App in any territory.*

## API Key
To access the API you'll need your own set of Credentials which consist of a <i>Developer ID</i> (dev_id) and an <i>Authentication Key</i> (auth_key).

Here are the Credentials for a sample account:

<table>
  <tr>
    <th>dev_id</th>
    <th>auth_key</th>
  </tr>
  <tr>
    <td>1004</td>
    <td>23DF3C7E9BD14D84BF892AD206B6755C</td>
  </tr>
</table>

Use your personal Credentials to access the API via a <i>Representational State Transfer</i> (<b>REST</b>) Web Service hosted at [http://api.{game}.com/{game}api.svc](#endpoint-base-urls).

### Obtaining API Key (Registration)
><i>An</i> [<b>``API Key``</b>](#api-key) <i>that will provide access to API.</i> The process of obtaining [<b>``API Key``</b>](#api-key) should be an one-time activity.

If you don't already have a dev_id and auth_key, please [<b>submit an application</b>](https://fs12.formsite.com/HiRez/form48/secure_index.html "Register to become developer") to gain access to the API.

If your application is accepted, you will receive an e-mail from [Hi-Rez Studios][hi_rez_studios] containing your personal [<b>``API Key``</b>](#api-key) within a few days.

<i>**NOTE**</i>: The same dev_id and auth_key combination should work for SmiteAPI, PaladinsAPI and RealmAPI, across all supported platforms. Do not request a new, if you already have a Credentials.

### Tokens and API Key Security

API keys should be treated as secret data and not exposed to users. To ensure the security of your [API key](#api-key), we strongly suggest that you make requests to the API server-side whenever possible.

Any requests to the API made via client-side present the risk of your API key being compromised. Most importantly, never include your [api_key](#api-key) inline in your code. For additional security, don't have the key itself contained anywhere in your code, keep it in a variable stored in a privately scoped method.

<!--
Any requests to the API made via client-side JavaScript present the risk of your API key being compromised. It is possible to partially obfuscate the key, but anything sent to the browser can be read by a determined user. Most importantly, never include your [api_key](#api-key) inline in the page. Keep any references to your [api_key](#api-key) in code that is contained in external javascript files which are included in the page. For additional security, don't have the key itself contained anywhere in your javascript code, but rather make an ajax call to load it, and keep it in a variable stored in a privately scoped method.
-->

## Endpoint Base URLs
To retrieve all information from the API, you will need to append all requests to the endpoint you want to retrieve data, and all requests must begin with the method you are wanting to access concatenated with the response type you are wanting.

  - [Paladins][paladins]: `http://api.paladins.com/paladinsapi.svc`
  - [Realm Royale][realm_royale]: `http://api.realmroyale.com/realmapi.svc`
  - [Smite][smite]: `http://api.smitegame.com/smiteapi.svc`

## Calling API Request's

><i>base_url_endpoint/method_pattern[response_format]/params</i><br/>The url format for calling a method from the api

<table>
  <tr>
    <th>URI Parameter</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>base_url_endpoint</td>
    <td>The URL prefix for the <a href="#endpoint-base-urls" title="Endpoints">Endpoint</a> that you want to use</td>
    <td>http://api.paladins.com/paladinsapi.svc</td>
  </tr>
  <tr>
    <td>method_pattern</td>
    <td>The pattern for the method above, where [response_format] is replaced by the <a href="./api-parameter-details.md#response-type" title="Response Type">formatting</a> that you want returned (either JSON or XML).</td>
    <td>/<a href="./create-session#create-session" title="Create Session">CreateSession</a>JSON</td>
  </tr>
  <tr>
    <td>params</td>
    <td>The method <a href="./api-parameter-details.md#api-parameter-details" title="API Parameters">params</a></td>
    <td>/{dev_id}/{signature}/{timestamp}</td>
  </tr>
</table>

##### URI example: http://api.paladins.com/paladinsapi.svc/CreateSessionJSON/{dev_id}/{signature}/{timestamp}

## Rate Limiting
The API rate limits in order to prevent abuse and over use of the API (either intentional, more likely unintentional “over use”). All API requests are subject to rate limits.

Rate limits are applied on a per-user basis  — or more accurately described, per dev_id / auth_key combination. By “per-user”, we mean that rate limits are shared across different endpoints and all supported platforms using the same dev_id.

Here are the default initial limitations for API Developers:
<table>
  <tr>
    <th style='text-align:center;vertical-align:middle'> Concurrent Sessions </th>
    <th style='text-align:center;vertical-align:middle'> Daily Sessions </th>
    <th style='text-align:center;vertical-align:middle'> Session Time </th>
    <th style='text-align:center;vertical-align:middle'> Daily Request </th>
  </tr>
  <tr>
    <td style='text-align:center;vertical-align:middle'> 50 </td>
    <td style='text-align:center;vertical-align:middle'> 500 </td>
    <td style='text-align:center;vertical-align:middle'> 15 minutes </td>
    <td style='text-align:center;vertical-align:middle'> 7500 </td>
  </tr>
</table>

### Exceeding a Rate Limit
Once a rate limit is reached, the API will return a [``ret_msg``](#ret_msg) containing details about the limit and any subsequent requests made by you will fail until the limit resets.

<!--
Rate Limits are tracked on an individual application
In the case that a rate limit is exceeded, the API will return a [``ret_msg``](#ret_msg) containing details about the limit  until the limit ends.
-->

### Tips to avoid being Rate Limited

<!-- ### Best practices
  - Spread out queries evenly between two time intervals to avoid sending traffic in spikes.
  - If Users are being throttled, be sure your app is not the cause. Reduce the user’s calls or spread the user’s calls more evenly over time.
  - Verify the error code and API endpoint to confirm the throttling type.
-->

#### Avoiding API Calls on Page Loads

Most rate limiting issues are caused by extraneous API calls. For example, don’t try to call the API on every page load of your website landing page. Instead, call the API infrequently and load the response into a [local cache](#caching). When users hit your website load the cached version of the results.

#### Caching

Store API responses in your application or on your site if you expect a lot of use. You may cache data locally wherever possible.

#### Checking for Errors

An invalid or rate limited request to the API will return a non-null [ret_msg](#ret_msg). Please check all API responses for errors.

#### Prioritize active users

If your site keeps track of many player (for example, fetching their current status or statistics about their game stats), consider only requesting data for users who have recently signed into your site.

#### Batch Processing

The API does not support requesting more than one resource with a single API call. However,  many ids can be handled in one API call using the [Get Player Batch](./get-player-batch#get-player-batch), [Get Player Batch From Match](./get-player-batch#get-player-batch) and [Get Match Details Batch](./get-player-batch#get-player-batch) endpoints.

We strongly recommend specify multiple IDs in one API request when possible as this improves performance of your API responses.

The following table illustrates this concept.
<table>
  <tr>
    <th align='center'>Example Request(s)</th>
    <th align='center'>Number of API Calls</th>
  </tr>
  <tr>
    <td style='text-align:center;vertical-align:middle'>
      /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id1}<br/>
      /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id2}<br/>
      /getplayer[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id3}
    </td>
    <td align='center'>3</td>
  </tr>
    <td style='text-align:center;vertical-align:middle'>
      /getplayerbatch[response_format]/{dev_id}/{signature}/{session_id}/{timestamp}/{player_id1},{player_id2},{player_id3}
    </td>
    <td align='center'>1</td>
  </tr>
</table>

## Session (Authentication)
><i>To begin using the API, you will first need to establish a valid Session.</i>

To Authenticating with the API, you may start a Session (via the [``CreateSession``](./create-session#create-session) method) and receive a <i>``session_id``</i>. Sessions are used for authentication, security, monitoring, and throttling. Once you obtain a <i>``Session``</i>, you will pass it to other methods for authentication.

More details regarding Session creation are provided in [``CreateSession``](./create-session#create-session).

### Refreshing Sessions

Sessions have expirations and must be recreated afterward, expirations do not affect existing Sessions.

Each session lasts for 15 minutes without activity (In other words, only when idle for 15 minutes).<br/>Each API call “resets the clock” . Sessions return an `timestamp` field indicating when a Session  was acquired.

However, you should build your applications in such a way that they are resilient to Session authentication failures. In other words, an application capable of refreshing Sessions should not need to know how long a Session will live. Rather, it should be prepared to deal with the Session becoming invalid at any time.

### Refresh in Response to Server Rejection for Bad Authentication

We recommend that you refresh your Sessions in response to being rejected by the server for bad authentication.

It is good practice to assume that your Session can expire or be revoked at any time, and refreshing reactively ensures that your application is prepared to deal with such situations as gracefully as possible. For this reason, refreshing in response to server rejection is preferable to refreshing proactively, on a fixed schedule.

When you make a request with expired or incorrect Session, the API returns a <a href="#ret-msg-invalid-session-id" title="Invalid Session Id">ret_msg error</a>.<!-- (with an invalid_token error)-->

## ret_msg
The API expose a field called “`ret_msg`” to represent an error or rate limit being encountered.

We recommend using this field value as an unique identifier for errors, with the exception of using the [``CreateSession``](./create-session#create-session) method or when the request completes without any error, the ret_msg will be not null when the request was not successful.

<table>
  <tr>
    <th align='center'> Message </th>
    <th align='center'> Description </th>
    <th align='center'> Recommendation </th>
  </tr>
  <tr>
    <td align='center' id='ret-msg-approved'> Approved </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that a new <a href="#session-authentication" title="Session">Session</a> has been created sucessful. </td>
    <td style='text-align:center;vertical-align:middle'> You may store the “session_id” is a local variable and use while it is valid. </td>
  </tr>
  <tr>
    <td align='center'> dailylimit </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that the dev_id used in the request has reached its rate limit and you may be unable to request new data. </td>
    <td style='text-align:center;vertical-align:middle'> You may wait until the limit ends. </td>
  </tr>
  <tr>
    <td align='center'> Daily request limit reached </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that the dev_id used in the request has reached its rate limit and you may be unable to request new data. </td>
    <td style='text-align:center;vertical-align:middle'> You may wait until the limit ends. </td>
  </tr>
  <tr>
    <td align='center'> Exceeded daily session cap. </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that the dev_id used in the request has reached its rate limit and you may be unable to request new data. </td>
    <td style='text-align:center;vertical-align:middle'> You may wait until the limit ends. </td>
  </tr>
  <tr>
    <td align='center'> Error while comparing Server and Client timestamp </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that the timestamp sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Exception while processing: Invalid date format </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that the timestamp sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Exception - Timestamp </td>
    <td style='text-align:center;vertical-align:middle'> This error means that your timestamp sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Exception - Timestamp Your signature: {signature} Your timestamp: {timestamp} Your session ID: {session_id} </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that the timestamp sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Exception while validating developer access.Invalid signature. </td>
    <td style='text-align:center;vertical-align:middle'> This error means that the method signature sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Failed to validate DeveloperId </td>
    <td style='text-align:center;vertical-align:middle'> This error means that your dev_id and/or auth_key sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Invalid date format </td>
    <td style='text-align:center;vertical-align:middle'> This error means that the date sent to the API was not determined to be valid format. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center' id='ret-msg-invalid-session-id'> Invalid session id. </td>
    <td style='text-align:center;vertical-align:middle'> This error means that the <a href="#session-authentication" title="Session">Session</a> sent was invalid or not alive, you may start a new session. </td>
    <td style='text-align:center;vertical-align:middle'> Use an existent/alive or start a new Session. </td>
  </tr>
  <tr>
    <td align='center'> Invalid signature.  Details ---> action={method_name} timestamp={timestamp} clientHash= self.generateSignature({method_name}) serverHash={server_hash} source=ValidateSession developer_id={dev_id} auth_key=HIDDEN' </td>
    <td style='text-align:center;vertical-align:middle'> This error means that the method signature sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Invalid signature </td>
    <td style='text-align:center;vertical-align:middle'> This error means that the method signature sent to the API was not determined to be valid. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Maximum number of active sessions reached. </td>
    <td style='text-align:center;vertical-align:middle'> Indicates that you have exceeded rate limits for <a href="#session-authentication" title="Session">Session</a> creation and you may be unable to create a new. </td>
    <td style='text-align:center;vertical-align:middle'>You may wait until the limit ends.</td>
  </tr>
  <tr>
    <td align='center'> No Match Details:{match_id} </td>
    <td style='text-align:center;vertical-align:middle'> The player was not found, has private account or haven't played any matches in the last 30 days </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Unauthorized Developer Id </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
  <tr>
    <td align='center'> Year, Month, and Day parameters describe an un-representable DateTime. </td>
    <td style='text-align:center;vertical-align:middle'> This error means that the date sent to the API was not determined to be valid format. </td>
    <td style='text-align:center;vertical-align:middle'>  </td>
  </tr>
</table>
<!--Or if the ret_msg is containing: dailylimit (7500 requests reached) / 404-->

## Best Practices

## Frequently Asked Questions (FAQ)

### What do we consider an API call?
- With the exception of using the [``Ping``](./ping#ping), all calls count towards the rate limits.

### Do all methods work with all endpoints?
- No. PC is the only endpoint guaranteed to work with all methods.

### How do I get my API Key?
- If you don't already have a [``API Key``](#api-key) (dev_id and auth_key) for PaladinsAPI, SmiteAPI or even RealmAPI, [click here](./../README.md#registration). If you already have, you can use your [``API Key``](#api-key) to connect to RealmAPI as well.

### Where do I find my API Key?
- If you've already requested your [``API Key``](#how-do-i-get-my-api-key), check your e-mail. If you can't found your API Key, send an e-mail to [Aaron](mailto:apugh@hirezstudios.com).

### How do I connect to the API?
- The API don't require a specific programming language to be used, so feel free to choose a language / tool that you are able to do ``Http Requests`` and read ``JSON`` and/or ``XML`` responses. If you want a wrapper, you can see them [here](./../README.md#wrappers).

### I got “Endpoint not Found” when I go to <http://api.{game}.com/{game}api.svc>.
- You will receive ``Endpoint not Found`` if you are trying to access a non-existent endpoint, submitting a invalid [Method Pattern](#calling-api-methods) or even trying to access it directly on your Web Browser.

### I'm getting “Maximum number of active sessions reached”. Is there way to close those current Sessions?
- Nop, Sessions are divided into 15 minute intervals. You may store the session_id and use it while is valid.

### I'm getting successful responses for the calls but the JSON / XML responses is null. What is happening?
- Did you already checked the ret_msg message? It's used to return a message error when the server-side catch an issue. You can check the ret_msg messages [**here**](#ret_msg). See also []().

### Why am I getting a null dataset for a player that exists?
- If a player has “Hide My Profile” enabled in-game, methods will return a null dataset.

### When using methods such as [``Get Match Details``](./get-match-details#get-match-details), some player info is missing. Why?
- If a player has “Hide My Profile” enabled in-game, some of their data will be unavailable for match history etc.

### How I could increase my API Access Limit?
- The first recommendation would be to use something like page caching or saving the data to a Database so you can poll it from your own database as often as needed. But if you already are doing it and think that is needed to increase your limit, drop an e-mail to [Aaron](mailto:apugh@hirezstudios.com).

### I have a question you didn't answer.
- [**Click here**](#getting-help) to check how you can get help!

## Known Bugs 🐞

The interface for each endpoint is identical. Therefore, a single application code-base should be able to support all supported platforms

However, since each endpoint is serviced by a unique Web Service, applications must create and maintain separate Sessions for each endpoint.  In other words, <del>you cannot use a Session ID created by the SmiteAPI endpoint (via the /createsession method) to make method calls to the PaladinsAPI endpoint.</del><sup id="session_id_exploit" class="reference"><a href="https://gist.github.com/luissilva1044894/c259d71fc7e7595d70d424c00ff5716b"  target="_blank"><span>[</span>1<span>]</span></a></sup>

[hi_rez_studios]: https://www.hirezstudios.com "Visit Hi-Rez Studios Website"
[paladins]: https://www.paladins.com/ "Paladins Game · Website"
[realm_royale]: https://www.realmroyale.com/ "Realm Royale Game · Website"
[smite]: https://www.smitegame.com/ "Smite Game · Website"
