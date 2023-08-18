/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.TitaniumLimit;
import org.openapitools.client.model.TitaniumOrderBy;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumChallengeListRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-18T12:50:05.891692Z[UTC]")
public class TitaniumChallengeListRequest {
  public static final String SERIALIZED_NAME_ASSET_ID = "assetId";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_CONSENSUS_RUN_TIMESTAMP = "consensusRunTimestamp";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_RUN_TIMESTAMP)
  private String consensusRunTimestamp;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_FILTER = "filter";
  @SerializedName(SERIALIZED_NAME_FILTER)
  private String filter;

  public static final String SERIALIZED_NAME_LIMIT = "limit";
  @SerializedName(SERIALIZED_NAME_LIMIT)
  private TitaniumLimit limit;

  public static final String SERIALIZED_NAME_OFFSET = "offset";
  @SerializedName(SERIALIZED_NAME_OFFSET)
  private Integer offset;

  public static final String SERIALIZED_NAME_ORDER_BY = "orderBy";
  @SerializedName(SERIALIZED_NAME_ORDER_BY)
  private TitaniumOrderBy orderBy;

  public static final String SERIALIZED_NAME_SNAP_TIME = "snapTime";
  @SerializedName(SERIALIZED_NAME_SNAP_TIME)
  private String snapTime;

  public static final String SERIALIZED_NAME_TRACE_NAME = "traceName";
  @SerializedName(SERIALIZED_NAME_TRACE_NAME)
  private String traceName;

  public TitaniumChallengeListRequest() { 
  }

  public TitaniumChallengeListRequest assetId(String assetId) {
    
    this.assetId = assetId;
    return this;
  }

   /**
   * Get assetId
   * @return assetId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAssetId() {
    return assetId;
  }


  public void setAssetId(String assetId) {
    this.assetId = assetId;
  }


  public TitaniumChallengeListRequest consensusRunTimestamp(String consensusRunTimestamp) {
    
    this.consensusRunTimestamp = consensusRunTimestamp;
    return this;
  }

   /**
   * Get consensusRunTimestamp
   * @return consensusRunTimestamp
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getConsensusRunTimestamp() {
    return consensusRunTimestamp;
  }


  public void setConsensusRunTimestamp(String consensusRunTimestamp) {
    this.consensusRunTimestamp = consensusRunTimestamp;
  }


  public TitaniumChallengeListRequest date(String date) {
    
    this.date = date;
    return this;
  }

   /**
   * Get date
   * @return date
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDate() {
    return date;
  }


  public void setDate(String date) {
    this.date = date;
  }


  public TitaniumChallengeListRequest filter(String filter) {
    
    this.filter = filter;
    return this;
  }

   /**
   * Get filter
   * @return filter
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getFilter() {
    return filter;
  }


  public void setFilter(String filter) {
    this.filter = filter;
  }


  public TitaniumChallengeListRequest limit(TitaniumLimit limit) {
    
    this.limit = limit;
    return this;
  }

   /**
   * Get limit
   * @return limit
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumLimit getLimit() {
    return limit;
  }


  public void setLimit(TitaniumLimit limit) {
    this.limit = limit;
  }


  public TitaniumChallengeListRequest offset(Integer offset) {
    
    this.offset = offset;
    return this;
  }

   /**
   * Get offset
   * @return offset
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getOffset() {
    return offset;
  }


  public void setOffset(Integer offset) {
    this.offset = offset;
  }


  public TitaniumChallengeListRequest orderBy(TitaniumOrderBy orderBy) {
    
    this.orderBy = orderBy;
    return this;
  }

   /**
   * Get orderBy
   * @return orderBy
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumOrderBy getOrderBy() {
    return orderBy;
  }


  public void setOrderBy(TitaniumOrderBy orderBy) {
    this.orderBy = orderBy;
  }


  public TitaniumChallengeListRequest snapTime(String snapTime) {
    
    this.snapTime = snapTime;
    return this;
  }

   /**
   * Get snapTime
   * @return snapTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSnapTime() {
    return snapTime;
  }


  public void setSnapTime(String snapTime) {
    this.snapTime = snapTime;
  }


  public TitaniumChallengeListRequest traceName(String traceName) {
    
    this.traceName = traceName;
    return this;
  }

   /**
   * Get traceName
   * @return traceName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTraceName() {
    return traceName;
  }


  public void setTraceName(String traceName) {
    this.traceName = traceName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumChallengeListRequest titaniumChallengeListRequest = (TitaniumChallengeListRequest) o;
    return Objects.equals(this.assetId, titaniumChallengeListRequest.assetId) &&
        Objects.equals(this.consensusRunTimestamp, titaniumChallengeListRequest.consensusRunTimestamp) &&
        Objects.equals(this.date, titaniumChallengeListRequest.date) &&
        Objects.equals(this.filter, titaniumChallengeListRequest.filter) &&
        Objects.equals(this.limit, titaniumChallengeListRequest.limit) &&
        Objects.equals(this.offset, titaniumChallengeListRequest.offset) &&
        Objects.equals(this.orderBy, titaniumChallengeListRequest.orderBy) &&
        Objects.equals(this.snapTime, titaniumChallengeListRequest.snapTime) &&
        Objects.equals(this.traceName, titaniumChallengeListRequest.traceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetId, consensusRunTimestamp, date, filter, limit, offset, orderBy, snapTime, traceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumChallengeListRequest {\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    consensusRunTimestamp: ").append(toIndentedString(consensusRunTimestamp)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    filter: ").append(toIndentedString(filter)).append("\n");
    sb.append("    limit: ").append(toIndentedString(limit)).append("\n");
    sb.append("    offset: ").append(toIndentedString(offset)).append("\n");
    sb.append("    orderBy: ").append(toIndentedString(orderBy)).append("\n");
    sb.append("    snapTime: ").append(toIndentedString(snapTime)).append("\n");
    sb.append("    traceName: ").append(toIndentedString(traceName)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("assetId");
    openapiFields.add("consensusRunTimestamp");
    openapiFields.add("date");
    openapiFields.add("filter");
    openapiFields.add("limit");
    openapiFields.add("offset");
    openapiFields.add("orderBy");
    openapiFields.add("snapTime");
    openapiFields.add("traceName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumChallengeListRequest
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumChallengeListRequest.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumChallengeListRequest is not found in the empty JSON string", TitaniumChallengeListRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumChallengeListRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumChallengeListRequest` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("assetId") != null && !jsonObj.get("assetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetId").toString()));
      }
      if (jsonObj.get("consensusRunTimestamp") != null && !jsonObj.get("consensusRunTimestamp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusRunTimestamp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusRunTimestamp").toString()));
      }
      if (jsonObj.get("date") != null && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if (jsonObj.get("filter") != null && !jsonObj.get("filter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `filter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("filter").toString()));
      }
      // validate the optional field `limit`
      if (jsonObj.getAsJsonObject("limit") != null) {
        TitaniumLimit.validateJsonObject(jsonObj.getAsJsonObject("limit"));
      }
      // validate the optional field `orderBy`
      if (jsonObj.getAsJsonObject("orderBy") != null) {
        TitaniumOrderBy.validateJsonObject(jsonObj.getAsJsonObject("orderBy"));
      }
      if (jsonObj.get("snapTime") != null && !jsonObj.get("snapTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snapTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snapTime").toString()));
      }
      if (jsonObj.get("traceName") != null && !jsonObj.get("traceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `traceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("traceName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumChallengeListRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumChallengeListRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumChallengeListRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumChallengeListRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumChallengeListRequest>() {
           @Override
           public void write(JsonWriter out, TitaniumChallengeListRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumChallengeListRequest read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumChallengeListRequest given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumChallengeListRequest
  * @throws IOException if the JSON string is invalid with respect to TitaniumChallengeListRequest
  */
  public static TitaniumChallengeListRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumChallengeListRequest.class);
  }

 /**
  * Convert an instance of TitaniumChallengeListRequest to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

