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
 * TitaniumChunk
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T18:51:10.560344Z[UTC]")
public class TitaniumChunk {
  public static final String SERIALIZED_NAME_ANNOTATION = "annotation";
  @SerializedName(SERIALIZED_NAME_ANNOTATION)
  private Object annotation;

  public static final String SERIALIZED_NAME_CHUNK_ID = "chunkId";
  @SerializedName(SERIALIZED_NAME_CHUNK_ID)
  private String chunkId;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ORIGINAL_FILE_NAME = "originalFileName";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_FILE_NAME)
  private String originalFileName;

  public static final String SERIALIZED_NAME_ROWS_COUNT = "rowsCount";
  @SerializedName(SERIALIZED_NAME_ROWS_COUNT)
  private Integer rowsCount;

  public static final String SERIALIZED_NAME_START_ROW = "startRow";
  @SerializedName(SERIALIZED_NAME_START_ROW)
  private Integer startRow;

  public static final String SERIALIZED_NAME_USER = "user";
  @SerializedName(SERIALIZED_NAME_USER)
  private String user;

  public TitaniumChunk() { 
  }

  public TitaniumChunk annotation(Object annotation) {
    
    this.annotation = annotation;
    return this;
  }

   /**
   * Get annotation
   * @return annotation
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAnnotation() {
    return annotation;
  }


  public void setAnnotation(Object annotation) {
    this.annotation = annotation;
  }


  public TitaniumChunk chunkId(String chunkId) {
    
    this.chunkId = chunkId;
    return this;
  }

   /**
   * Get chunkId
   * @return chunkId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getChunkId() {
    return chunkId;
  }


  public void setChunkId(String chunkId) {
    this.chunkId = chunkId;
  }


  public TitaniumChunk description(String description) {
    
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


  public TitaniumChunk originalFileName(String originalFileName) {
    
    this.originalFileName = originalFileName;
    return this;
  }

   /**
   * Get originalFileName
   * @return originalFileName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOriginalFileName() {
    return originalFileName;
  }


  public void setOriginalFileName(String originalFileName) {
    this.originalFileName = originalFileName;
  }


  public TitaniumChunk rowsCount(Integer rowsCount) {
    
    this.rowsCount = rowsCount;
    return this;
  }

   /**
   * Get rowsCount
   * @return rowsCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getRowsCount() {
    return rowsCount;
  }


  public void setRowsCount(Integer rowsCount) {
    this.rowsCount = rowsCount;
  }


  public TitaniumChunk startRow(Integer startRow) {
    
    this.startRow = startRow;
    return this;
  }

   /**
   * Get startRow
   * @return startRow
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getStartRow() {
    return startRow;
  }


  public void setStartRow(Integer startRow) {
    this.startRow = startRow;
  }


  public TitaniumChunk user(String user) {
    
    this.user = user;
    return this;
  }

   /**
   * Get user
   * @return user
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getUser() {
    return user;
  }


  public void setUser(String user) {
    this.user = user;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumChunk titaniumChunk = (TitaniumChunk) o;
    return Objects.equals(this.annotation, titaniumChunk.annotation) &&
        Objects.equals(this.chunkId, titaniumChunk.chunkId) &&
        Objects.equals(this.description, titaniumChunk.description) &&
        Objects.equals(this.originalFileName, titaniumChunk.originalFileName) &&
        Objects.equals(this.rowsCount, titaniumChunk.rowsCount) &&
        Objects.equals(this.startRow, titaniumChunk.startRow) &&
        Objects.equals(this.user, titaniumChunk.user);
  }

  @Override
  public int hashCode() {
    return Objects.hash(annotation, chunkId, description, originalFileName, rowsCount, startRow, user);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumChunk {\n");
    sb.append("    annotation: ").append(toIndentedString(annotation)).append("\n");
    sb.append("    chunkId: ").append(toIndentedString(chunkId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    originalFileName: ").append(toIndentedString(originalFileName)).append("\n");
    sb.append("    rowsCount: ").append(toIndentedString(rowsCount)).append("\n");
    sb.append("    startRow: ").append(toIndentedString(startRow)).append("\n");
    sb.append("    user: ").append(toIndentedString(user)).append("\n");
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
    openapiFields.add("annotation");
    openapiFields.add("chunkId");
    openapiFields.add("description");
    openapiFields.add("originalFileName");
    openapiFields.add("rowsCount");
    openapiFields.add("startRow");
    openapiFields.add("user");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumChunk
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumChunk.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumChunk is not found in the empty JSON string", TitaniumChunk.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumChunk.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumChunk` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("chunkId") != null && !jsonObj.get("chunkId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `chunkId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("chunkId").toString()));
      }
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("originalFileName") != null && !jsonObj.get("originalFileName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `originalFileName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("originalFileName").toString()));
      }
      if (jsonObj.get("user") != null && !jsonObj.get("user").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumChunk.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumChunk' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumChunk> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumChunk.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumChunk>() {
           @Override
           public void write(JsonWriter out, TitaniumChunk value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumChunk read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumChunk given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumChunk
  * @throws IOException if the JSON string is invalid with respect to TitaniumChunk
  */
  public static TitaniumChunk fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumChunk.class);
  }

 /**
  * Convert an instance of TitaniumChunk to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

