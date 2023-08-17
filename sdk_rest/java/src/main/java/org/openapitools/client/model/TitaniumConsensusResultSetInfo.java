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
 * TitaniumConsensusResultSetInfo
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-17T15:40:04.150653Z[UTC]")
public class TitaniumConsensusResultSetInfo {
  public static final String SERIALIZED_NAME_COHORT_NAME = "cohortName";
  @SerializedName(SERIALIZED_NAME_COHORT_NAME)
  private String cohortName;

  public static final String SERIALIZED_NAME_CONSENSUS_RESULT_SET_ID = "consensusResultSetId";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_RESULT_SET_ID)
  private String consensusResultSetId;

  public static final String SERIALIZED_NAME_CONSENSUS_RUN_TIMESTAMP = "consensusRunTimestamp";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_RUN_TIMESTAMP)
  private String consensusRunTimestamp;

  public static final String SERIALIZED_NAME_DATA_CONTENT = "dataContent";
  @SerializedName(SERIALIZED_NAME_DATA_CONTENT)
  private String dataContent;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public TitaniumConsensusResultSetInfo() { 
  }

  public TitaniumConsensusResultSetInfo cohortName(String cohortName) {
    
    this.cohortName = cohortName;
    return this;
  }

   /**
   * Get cohortName
   * @return cohortName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getCohortName() {
    return cohortName;
  }


  public void setCohortName(String cohortName) {
    this.cohortName = cohortName;
  }


  public TitaniumConsensusResultSetInfo consensusResultSetId(String consensusResultSetId) {
    
    this.consensusResultSetId = consensusResultSetId;
    return this;
  }

   /**
   * Get consensusResultSetId
   * @return consensusResultSetId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getConsensusResultSetId() {
    return consensusResultSetId;
  }


  public void setConsensusResultSetId(String consensusResultSetId) {
    this.consensusResultSetId = consensusResultSetId;
  }


  public TitaniumConsensusResultSetInfo consensusRunTimestamp(String consensusRunTimestamp) {
    
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


  public TitaniumConsensusResultSetInfo dataContent(String dataContent) {
    
    this.dataContent = dataContent;
    return this;
  }

   /**
   * Get dataContent
   * @return dataContent
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDataContent() {
    return dataContent;
  }


  public void setDataContent(String dataContent) {
    this.dataContent = dataContent;
  }


  public TitaniumConsensusResultSetInfo description(String description) {
    
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDescription() {
    return description;
  }


  public void setDescription(String description) {
    this.description = description;
  }


  public TitaniumConsensusResultSetInfo status(String status) {
    
    this.status = status;
    return this;
  }

   /**
   * Get status
   * @return status
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getStatus() {
    return status;
  }


  public void setStatus(String status) {
    this.status = status;
  }


  public TitaniumConsensusResultSetInfo type(String type) {
    
    this.type = type;
    return this;
  }

   /**
   * Get type
   * @return type
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getType() {
    return type;
  }


  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumConsensusResultSetInfo titaniumConsensusResultSetInfo = (TitaniumConsensusResultSetInfo) o;
    return Objects.equals(this.cohortName, titaniumConsensusResultSetInfo.cohortName) &&
        Objects.equals(this.consensusResultSetId, titaniumConsensusResultSetInfo.consensusResultSetId) &&
        Objects.equals(this.consensusRunTimestamp, titaniumConsensusResultSetInfo.consensusRunTimestamp) &&
        Objects.equals(this.dataContent, titaniumConsensusResultSetInfo.dataContent) &&
        Objects.equals(this.description, titaniumConsensusResultSetInfo.description) &&
        Objects.equals(this.status, titaniumConsensusResultSetInfo.status) &&
        Objects.equals(this.type, titaniumConsensusResultSetInfo.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cohortName, consensusResultSetId, consensusRunTimestamp, dataContent, description, status, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumConsensusResultSetInfo {\n");
    sb.append("    cohortName: ").append(toIndentedString(cohortName)).append("\n");
    sb.append("    consensusResultSetId: ").append(toIndentedString(consensusResultSetId)).append("\n");
    sb.append("    consensusRunTimestamp: ").append(toIndentedString(consensusRunTimestamp)).append("\n");
    sb.append("    dataContent: ").append(toIndentedString(dataContent)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("cohortName");
    openapiFields.add("consensusResultSetId");
    openapiFields.add("consensusRunTimestamp");
    openapiFields.add("dataContent");
    openapiFields.add("description");
    openapiFields.add("status");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumConsensusResultSetInfo
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumConsensusResultSetInfo.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumConsensusResultSetInfo is not found in the empty JSON string", TitaniumConsensusResultSetInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumConsensusResultSetInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumConsensusResultSetInfo` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("cohortName") != null && !jsonObj.get("cohortName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cohortName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cohortName").toString()));
      }
      if (jsonObj.get("consensusResultSetId") != null && !jsonObj.get("consensusResultSetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusResultSetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusResultSetId").toString()));
      }
      if (jsonObj.get("consensusRunTimestamp") != null && !jsonObj.get("consensusRunTimestamp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusRunTimestamp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusRunTimestamp").toString()));
      }
      if (jsonObj.get("dataContent") != null && !jsonObj.get("dataContent").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dataContent` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dataContent").toString()));
      }
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumConsensusResultSetInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumConsensusResultSetInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumConsensusResultSetInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumConsensusResultSetInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumConsensusResultSetInfo>() {
           @Override
           public void write(JsonWriter out, TitaniumConsensusResultSetInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumConsensusResultSetInfo read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumConsensusResultSetInfo given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumConsensusResultSetInfo
  * @throws IOException if the JSON string is invalid with respect to TitaniumConsensusResultSetInfo
  */
  public static TitaniumConsensusResultSetInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumConsensusResultSetInfo.class);
  }

 /**
  * Convert an instance of TitaniumConsensusResultSetInfo to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

