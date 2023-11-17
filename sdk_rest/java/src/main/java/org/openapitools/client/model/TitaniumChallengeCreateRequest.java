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
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TitaniumAttachment;

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
 * TitaniumChallengeCreateRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T18:52:15.032311Z[UTC]")
public class TitaniumChallengeCreateRequest {
  public static final String SERIALIZED_NAME_ASSET_ID = "assetId";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_ATTACHMENTS = "attachments";
  @SerializedName(SERIALIZED_NAME_ATTACHMENTS)
  private List<TitaniumAttachment> attachments = null;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_EVIDENCE_TYPE = "evidenceType";
  @SerializedName(SERIALIZED_NAME_EVIDENCE_TYPE)
  private String evidenceType;

  public static final String SERIALIZED_NAME_GENERAL_FIELDS = "generalFields";
  @SerializedName(SERIALIZED_NAME_GENERAL_FIELDS)
  private List<String> generalFields = null;

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_SUBMITTED_DATE = "submittedDate";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_DATE)
  private String submittedDate;

  public static final String SERIALIZED_NAME_SUBMITTED_ID = "submittedId";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_ID)
  private String submittedId;

  public static final String SERIALIZED_NAME_SUBMITTED_URL = "submittedUrl";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_URL)
  private String submittedUrl;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private String time;

  public static final String SERIALIZED_NAME_TRACE_NAME = "traceName";
  @SerializedName(SERIALIZED_NAME_TRACE_NAME)
  private String traceName;

  public TitaniumChallengeCreateRequest() { 
  }

  public TitaniumChallengeCreateRequest assetId(String assetId) {
    
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


  public TitaniumChallengeCreateRequest attachments(List<TitaniumAttachment> attachments) {
    
    this.attachments = attachments;
    return this;
  }

  public TitaniumChallengeCreateRequest addAttachmentsItem(TitaniumAttachment attachmentsItem) {
    if (this.attachments == null) {
      this.attachments = new ArrayList<>();
    }
    this.attachments.add(attachmentsItem);
    return this;
  }

   /**
   * Get attachments
   * @return attachments
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumAttachment> getAttachments() {
    return attachments;
  }


  public void setAttachments(List<TitaniumAttachment> attachments) {
    this.attachments = attachments;
  }


  public TitaniumChallengeCreateRequest date(String date) {
    
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


  public TitaniumChallengeCreateRequest evidenceType(String evidenceType) {
    
    this.evidenceType = evidenceType;
    return this;
  }

   /**
   * Get evidenceType
   * @return evidenceType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEvidenceType() {
    return evidenceType;
  }


  public void setEvidenceType(String evidenceType) {
    this.evidenceType = evidenceType;
  }


  public TitaniumChallengeCreateRequest generalFields(List<String> generalFields) {
    
    this.generalFields = generalFields;
    return this;
  }

  public TitaniumChallengeCreateRequest addGeneralFieldsItem(String generalFieldsItem) {
    if (this.generalFields == null) {
      this.generalFields = new ArrayList<>();
    }
    this.generalFields.add(generalFieldsItem);
    return this;
  }

   /**
   * Get generalFields
   * @return generalFields
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getGeneralFields() {
    return generalFields;
  }


  public void setGeneralFields(List<String> generalFields) {
    this.generalFields = generalFields;
  }


  public TitaniumChallengeCreateRequest note(String note) {
    
    this.note = note;
    return this;
  }

   /**
   * Get note
   * @return note
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getNote() {
    return note;
  }


  public void setNote(String note) {
    this.note = note;
  }


  public TitaniumChallengeCreateRequest submittedDate(String submittedDate) {
    
    this.submittedDate = submittedDate;
    return this;
  }

   /**
   * Get submittedDate
   * @return submittedDate
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubmittedDate() {
    return submittedDate;
  }


  public void setSubmittedDate(String submittedDate) {
    this.submittedDate = submittedDate;
  }


  public TitaniumChallengeCreateRequest submittedId(String submittedId) {
    
    this.submittedId = submittedId;
    return this;
  }

   /**
   * Get submittedId
   * @return submittedId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubmittedId() {
    return submittedId;
  }


  public void setSubmittedId(String submittedId) {
    this.submittedId = submittedId;
  }


  public TitaniumChallengeCreateRequest submittedUrl(String submittedUrl) {
    
    this.submittedUrl = submittedUrl;
    return this;
  }

   /**
   * Get submittedUrl
   * @return submittedUrl
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubmittedUrl() {
    return submittedUrl;
  }


  public void setSubmittedUrl(String submittedUrl) {
    this.submittedUrl = submittedUrl;
  }


  public TitaniumChallengeCreateRequest time(String time) {
    
    this.time = time;
    return this;
  }

   /**
   * Get time
   * @return time
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTime() {
    return time;
  }


  public void setTime(String time) {
    this.time = time;
  }


  public TitaniumChallengeCreateRequest traceName(String traceName) {
    
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
    TitaniumChallengeCreateRequest titaniumChallengeCreateRequest = (TitaniumChallengeCreateRequest) o;
    return Objects.equals(this.assetId, titaniumChallengeCreateRequest.assetId) &&
        Objects.equals(this.attachments, titaniumChallengeCreateRequest.attachments) &&
        Objects.equals(this.date, titaniumChallengeCreateRequest.date) &&
        Objects.equals(this.evidenceType, titaniumChallengeCreateRequest.evidenceType) &&
        Objects.equals(this.generalFields, titaniumChallengeCreateRequest.generalFields) &&
        Objects.equals(this.note, titaniumChallengeCreateRequest.note) &&
        Objects.equals(this.submittedDate, titaniumChallengeCreateRequest.submittedDate) &&
        Objects.equals(this.submittedId, titaniumChallengeCreateRequest.submittedId) &&
        Objects.equals(this.submittedUrl, titaniumChallengeCreateRequest.submittedUrl) &&
        Objects.equals(this.time, titaniumChallengeCreateRequest.time) &&
        Objects.equals(this.traceName, titaniumChallengeCreateRequest.traceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetId, attachments, date, evidenceType, generalFields, note, submittedDate, submittedId, submittedUrl, time, traceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumChallengeCreateRequest {\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    attachments: ").append(toIndentedString(attachments)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    evidenceType: ").append(toIndentedString(evidenceType)).append("\n");
    sb.append("    generalFields: ").append(toIndentedString(generalFields)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    submittedDate: ").append(toIndentedString(submittedDate)).append("\n");
    sb.append("    submittedId: ").append(toIndentedString(submittedId)).append("\n");
    sb.append("    submittedUrl: ").append(toIndentedString(submittedUrl)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
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
    openapiFields.add("attachments");
    openapiFields.add("date");
    openapiFields.add("evidenceType");
    openapiFields.add("generalFields");
    openapiFields.add("note");
    openapiFields.add("submittedDate");
    openapiFields.add("submittedId");
    openapiFields.add("submittedUrl");
    openapiFields.add("time");
    openapiFields.add("traceName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumChallengeCreateRequest
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumChallengeCreateRequest.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumChallengeCreateRequest is not found in the empty JSON string", TitaniumChallengeCreateRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumChallengeCreateRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumChallengeCreateRequest` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("assetId") != null && !jsonObj.get("assetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetId").toString()));
      }
      JsonArray jsonArrayattachments = jsonObj.getAsJsonArray("attachments");
      if (jsonArrayattachments != null) {
        // ensure the json data is an array
        if (!jsonObj.get("attachments").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `attachments` to be an array in the JSON string but got `%s`", jsonObj.get("attachments").toString()));
        }

        // validate the optional field `attachments` (array)
        for (int i = 0; i < jsonArrayattachments.size(); i++) {
          TitaniumAttachment.validateJsonObject(jsonArrayattachments.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("date") != null && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if (jsonObj.get("evidenceType") != null && !jsonObj.get("evidenceType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `evidenceType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("evidenceType").toString()));
      }
      // ensure the json data is an array
      if (jsonObj.get("generalFields") != null && !jsonObj.get("generalFields").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `generalFields` to be an array in the JSON string but got `%s`", jsonObj.get("generalFields").toString()));
      }
      if (jsonObj.get("note") != null && !jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
      if (jsonObj.get("submittedDate") != null && !jsonObj.get("submittedDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submittedDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submittedDate").toString()));
      }
      if (jsonObj.get("submittedId") != null && !jsonObj.get("submittedId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submittedId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submittedId").toString()));
      }
      if (jsonObj.get("submittedUrl") != null && !jsonObj.get("submittedUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submittedUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submittedUrl").toString()));
      }
      if (jsonObj.get("time") != null && !jsonObj.get("time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("time").toString()));
      }
      if (jsonObj.get("traceName") != null && !jsonObj.get("traceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `traceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("traceName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumChallengeCreateRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumChallengeCreateRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumChallengeCreateRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumChallengeCreateRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumChallengeCreateRequest>() {
           @Override
           public void write(JsonWriter out, TitaniumChallengeCreateRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumChallengeCreateRequest read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumChallengeCreateRequest given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumChallengeCreateRequest
  * @throws IOException if the JSON string is invalid with respect to TitaniumChallengeCreateRequest
  */
  public static TitaniumChallengeCreateRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumChallengeCreateRequest.class);
  }

 /**
  * Convert an instance of TitaniumChallengeCreateRequest to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

