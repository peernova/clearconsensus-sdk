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
import org.openapitools.client.model.TitaniumCollapseTableRequest;
import org.openapitools.client.model.TitaniumTableRequest;

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
 * TitaniumConsensusTabRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T09:47:12.614194Z[UTC]")
public class TitaniumConsensusTabRequest {
  public static final String SERIALIZED_NAME_ASSET_ID = "assetId";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_COLLAPSE_TABLE_CONFIG = "collapseTableConfig";
  @SerializedName(SERIALIZED_NAME_COLLAPSE_TABLE_CONFIG)
  private TitaniumCollapseTableRequest collapseTableConfig;

  public static final String SERIALIZED_NAME_CONSENSUS_RUN_TIMESTAMP = "consensusRunTimestamp";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_RUN_TIMESTAMP)
  private String consensusRunTimestamp;

  public static final String SERIALIZED_NAME_DATA_TYPE = "dataType";
  @SerializedName(SERIALIZED_NAME_DATA_TYPE)
  private String dataType;

  public static final String SERIALIZED_NAME_TABLE_CONFIG = "tableConfig";
  @SerializedName(SERIALIZED_NAME_TABLE_CONFIG)
  private TitaniumTableRequest tableConfig;

  public static final String SERIALIZED_NAME_TRACE_NAME = "traceName";
  @SerializedName(SERIALIZED_NAME_TRACE_NAME)
  private String traceName;

  public TitaniumConsensusTabRequest() { 
  }

  public TitaniumConsensusTabRequest assetId(String assetId) {
    
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


  public TitaniumConsensusTabRequest collapseTableConfig(TitaniumCollapseTableRequest collapseTableConfig) {
    
    this.collapseTableConfig = collapseTableConfig;
    return this;
  }

   /**
   * Get collapseTableConfig
   * @return collapseTableConfig
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumCollapseTableRequest getCollapseTableConfig() {
    return collapseTableConfig;
  }


  public void setCollapseTableConfig(TitaniumCollapseTableRequest collapseTableConfig) {
    this.collapseTableConfig = collapseTableConfig;
  }


  public TitaniumConsensusTabRequest consensusRunTimestamp(String consensusRunTimestamp) {
    
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


  public TitaniumConsensusTabRequest dataType(String dataType) {
    
    this.dataType = dataType;
    return this;
  }

   /**
   * Get dataType
   * @return dataType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDataType() {
    return dataType;
  }


  public void setDataType(String dataType) {
    this.dataType = dataType;
  }


  public TitaniumConsensusTabRequest tableConfig(TitaniumTableRequest tableConfig) {
    
    this.tableConfig = tableConfig;
    return this;
  }

   /**
   * Get tableConfig
   * @return tableConfig
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumTableRequest getTableConfig() {
    return tableConfig;
  }


  public void setTableConfig(TitaniumTableRequest tableConfig) {
    this.tableConfig = tableConfig;
  }


  public TitaniumConsensusTabRequest traceName(String traceName) {
    
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
    TitaniumConsensusTabRequest titaniumConsensusTabRequest = (TitaniumConsensusTabRequest) o;
    return Objects.equals(this.assetId, titaniumConsensusTabRequest.assetId) &&
        Objects.equals(this.collapseTableConfig, titaniumConsensusTabRequest.collapseTableConfig) &&
        Objects.equals(this.consensusRunTimestamp, titaniumConsensusTabRequest.consensusRunTimestamp) &&
        Objects.equals(this.dataType, titaniumConsensusTabRequest.dataType) &&
        Objects.equals(this.tableConfig, titaniumConsensusTabRequest.tableConfig) &&
        Objects.equals(this.traceName, titaniumConsensusTabRequest.traceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetId, collapseTableConfig, consensusRunTimestamp, dataType, tableConfig, traceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumConsensusTabRequest {\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    collapseTableConfig: ").append(toIndentedString(collapseTableConfig)).append("\n");
    sb.append("    consensusRunTimestamp: ").append(toIndentedString(consensusRunTimestamp)).append("\n");
    sb.append("    dataType: ").append(toIndentedString(dataType)).append("\n");
    sb.append("    tableConfig: ").append(toIndentedString(tableConfig)).append("\n");
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
    openapiFields.add("collapseTableConfig");
    openapiFields.add("consensusRunTimestamp");
    openapiFields.add("dataType");
    openapiFields.add("tableConfig");
    openapiFields.add("traceName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumConsensusTabRequest
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumConsensusTabRequest.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumConsensusTabRequest is not found in the empty JSON string", TitaniumConsensusTabRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumConsensusTabRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumConsensusTabRequest` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("assetId") != null && !jsonObj.get("assetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetId").toString()));
      }
      // validate the optional field `collapseTableConfig`
      if (jsonObj.getAsJsonObject("collapseTableConfig") != null) {
        TitaniumCollapseTableRequest.validateJsonObject(jsonObj.getAsJsonObject("collapseTableConfig"));
      }
      if (jsonObj.get("consensusRunTimestamp") != null && !jsonObj.get("consensusRunTimestamp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusRunTimestamp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusRunTimestamp").toString()));
      }
      if (jsonObj.get("dataType") != null && !jsonObj.get("dataType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dataType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dataType").toString()));
      }
      // validate the optional field `tableConfig`
      if (jsonObj.getAsJsonObject("tableConfig") != null) {
        TitaniumTableRequest.validateJsonObject(jsonObj.getAsJsonObject("tableConfig"));
      }
      if (jsonObj.get("traceName") != null && !jsonObj.get("traceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `traceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("traceName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumConsensusTabRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumConsensusTabRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumConsensusTabRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumConsensusTabRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumConsensusTabRequest>() {
           @Override
           public void write(JsonWriter out, TitaniumConsensusTabRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumConsensusTabRequest read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumConsensusTabRequest given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumConsensusTabRequest
  * @throws IOException if the JSON string is invalid with respect to TitaniumConsensusTabRequest
  */
  public static TitaniumConsensusTabRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumConsensusTabRequest.class);
  }

 /**
  * Convert an instance of TitaniumConsensusTabRequest to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

