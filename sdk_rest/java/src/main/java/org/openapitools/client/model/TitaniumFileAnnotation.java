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
import org.openapitools.client.model.TitaniumAssetDetails;
import org.openapitools.client.model.TitaniumChunk;

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
 * TitaniumFileAnnotation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:53:32.718826Z[UTC]")
public class TitaniumFileAnnotation {
  public static final String SERIALIZED_NAME_ANNOTATION = "annotation";
  @SerializedName(SERIALIZED_NAME_ANNOTATION)
  private Object annotation;

  public static final String SERIALIZED_NAME_ASSET = "asset";
  @SerializedName(SERIALIZED_NAME_ASSET)
  private TitaniumAssetDetails asset;

  public static final String SERIALIZED_NAME_CHUNKS = "chunks";
  @SerializedName(SERIALIZED_NAME_CHUNKS)
  private List<TitaniumChunk> chunks = null;

  public static final String SERIALIZED_NAME_CLIENT = "client";
  @SerializedName(SERIALIZED_NAME_CLIENT)
  private String client;

  public static final String SERIALIZED_NAME_FILE_NAME = "fileName";
  @SerializedName(SERIALIZED_NAME_FILE_NAME)
  private String fileName;

  public static final String SERIALIZED_NAME_MODE = "mode";
  @SerializedName(SERIALIZED_NAME_MODE)
  private String mode;

  public static final String SERIALIZED_NAME_UPLOAD_TIME = "uploadTime";
  @SerializedName(SERIALIZED_NAME_UPLOAD_TIME)
  private String uploadTime;

  public TitaniumFileAnnotation() { 
  }

  public TitaniumFileAnnotation annotation(Object annotation) {
    
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


  public TitaniumFileAnnotation asset(TitaniumAssetDetails asset) {
    
    this.asset = asset;
    return this;
  }

   /**
   * Get asset
   * @return asset
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumAssetDetails getAsset() {
    return asset;
  }


  public void setAsset(TitaniumAssetDetails asset) {
    this.asset = asset;
  }


  public TitaniumFileAnnotation chunks(List<TitaniumChunk> chunks) {
    
    this.chunks = chunks;
    return this;
  }

  public TitaniumFileAnnotation addChunksItem(TitaniumChunk chunksItem) {
    if (this.chunks == null) {
      this.chunks = new ArrayList<>();
    }
    this.chunks.add(chunksItem);
    return this;
  }

   /**
   * Get chunks
   * @return chunks
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumChunk> getChunks() {
    return chunks;
  }


  public void setChunks(List<TitaniumChunk> chunks) {
    this.chunks = chunks;
  }


  public TitaniumFileAnnotation client(String client) {
    
    this.client = client;
    return this;
  }

   /**
   * Get client
   * @return client
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getClient() {
    return client;
  }


  public void setClient(String client) {
    this.client = client;
  }


  public TitaniumFileAnnotation fileName(String fileName) {
    
    this.fileName = fileName;
    return this;
  }

   /**
   * Get fileName
   * @return fileName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getFileName() {
    return fileName;
  }


  public void setFileName(String fileName) {
    this.fileName = fileName;
  }


  public TitaniumFileAnnotation mode(String mode) {
    
    this.mode = mode;
    return this;
  }

   /**
   * Get mode
   * @return mode
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getMode() {
    return mode;
  }


  public void setMode(String mode) {
    this.mode = mode;
  }


  public TitaniumFileAnnotation uploadTime(String uploadTime) {
    
    this.uploadTime = uploadTime;
    return this;
  }

   /**
   * Get uploadTime
   * @return uploadTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getUploadTime() {
    return uploadTime;
  }


  public void setUploadTime(String uploadTime) {
    this.uploadTime = uploadTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumFileAnnotation titaniumFileAnnotation = (TitaniumFileAnnotation) o;
    return Objects.equals(this.annotation, titaniumFileAnnotation.annotation) &&
        Objects.equals(this.asset, titaniumFileAnnotation.asset) &&
        Objects.equals(this.chunks, titaniumFileAnnotation.chunks) &&
        Objects.equals(this.client, titaniumFileAnnotation.client) &&
        Objects.equals(this.fileName, titaniumFileAnnotation.fileName) &&
        Objects.equals(this.mode, titaniumFileAnnotation.mode) &&
        Objects.equals(this.uploadTime, titaniumFileAnnotation.uploadTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(annotation, asset, chunks, client, fileName, mode, uploadTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumFileAnnotation {\n");
    sb.append("    annotation: ").append(toIndentedString(annotation)).append("\n");
    sb.append("    asset: ").append(toIndentedString(asset)).append("\n");
    sb.append("    chunks: ").append(toIndentedString(chunks)).append("\n");
    sb.append("    client: ").append(toIndentedString(client)).append("\n");
    sb.append("    fileName: ").append(toIndentedString(fileName)).append("\n");
    sb.append("    mode: ").append(toIndentedString(mode)).append("\n");
    sb.append("    uploadTime: ").append(toIndentedString(uploadTime)).append("\n");
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
    openapiFields.add("asset");
    openapiFields.add("chunks");
    openapiFields.add("client");
    openapiFields.add("fileName");
    openapiFields.add("mode");
    openapiFields.add("uploadTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumFileAnnotation
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumFileAnnotation.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumFileAnnotation is not found in the empty JSON string", TitaniumFileAnnotation.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumFileAnnotation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumFileAnnotation` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `asset`
      if (jsonObj.getAsJsonObject("asset") != null) {
        TitaniumAssetDetails.validateJsonObject(jsonObj.getAsJsonObject("asset"));
      }
      JsonArray jsonArraychunks = jsonObj.getAsJsonArray("chunks");
      if (jsonArraychunks != null) {
        // ensure the json data is an array
        if (!jsonObj.get("chunks").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `chunks` to be an array in the JSON string but got `%s`", jsonObj.get("chunks").toString()));
        }

        // validate the optional field `chunks` (array)
        for (int i = 0; i < jsonArraychunks.size(); i++) {
          TitaniumChunk.validateJsonObject(jsonArraychunks.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("client") != null && !jsonObj.get("client").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client").toString()));
      }
      if (jsonObj.get("fileName") != null && !jsonObj.get("fileName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileName").toString()));
      }
      if (jsonObj.get("mode") != null && !jsonObj.get("mode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mode").toString()));
      }
      if (jsonObj.get("uploadTime") != null && !jsonObj.get("uploadTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uploadTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uploadTime").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumFileAnnotation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumFileAnnotation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumFileAnnotation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumFileAnnotation.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumFileAnnotation>() {
           @Override
           public void write(JsonWriter out, TitaniumFileAnnotation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumFileAnnotation read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumFileAnnotation given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumFileAnnotation
  * @throws IOException if the JSON string is invalid with respect to TitaniumFileAnnotation
  */
  public static TitaniumFileAnnotation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumFileAnnotation.class);
  }

 /**
  * Convert an instance of TitaniumFileAnnotation to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

